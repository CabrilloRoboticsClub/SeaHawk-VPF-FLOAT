'''
code.py

SeaHawk Vertical Profiling Float Code

Copyright (C) 2022-2023 Cabrillo Robotics Club

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Cabrillo Robotics Club
6500 Soquel Drive Aptos, CA 95003
cabrillorobotics@gmail.com
'''

# # # # # # # #
# CONSTANTS
# # # # # # # #

# team number as defined by MATE
TEAM_NUM = "PN03"

# LoRa Device ID for the Float Transceiver
FLOAT_LORA_ID = 18

# LoRa Device ID for the Deck Transceiver
DECK_LORA_ID = 28

# number of seconds to wait on the surface transmitting before diving again
TRANSMIT_DURATION = 10

# number of seconds it takes for the pump to fill the tank
BILGE_FILL_DURATION = 5

# number of seconds it takes for the float to sink to the bottom
DIVE_DURATION = 5

# number of seconds it takes for the pump to empty the tank
BILGE_EMPTY_DURATION = 5

# number of seconds it takes for the float to rise to the surface
SURFACE_DURATION = 5


# # # # # # # #
# IMPORTS
# # # # # # # #

import time
import board
import busio
import digitalio
from adafruit_motorkit import MotorKit

# lora radio library
import adafruit_rfm9x


# # # # # # # # #
# BUS SETUP
# # # # # # # # #

# instantiate the spi interface
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# LoRa Module Chip Select on Digital Pin 5
CS = digitalio.DigitalInOut(board.D5)

# LoRa Module Reset on Digital Pin 6
RESET = digitalio.DigitalInOut(board.D6)

# set the radio frequency to 915mhz (NOT 868)
RADIO_FREQ_MHZ = 915.0 


# # # # # # # #
# LoRa Radio Wing SETUP
# # # # # # # #

# instantiate the lora radio in 915mhz mode
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# set my lora node ID
# I am the float
rfm9x.node = FLOAT_LORA_ID

# set the destination lora node ID
# destination is deck
rfm9x.destination = DECK_LORA_ID


# # # # # # # #
# MotorKit SETUP
# # # # # # # #

# Set up the motor kit
kit = MotorKit()

# stop motors on init
# incase a power cycle happens while motors are running
kit.motor1.throttle = 0.0
kit.motor2.throttle = 0.0


# # # # # # # #
# Functions
# # # # # # # #

# transmit the time in seconds
def transmit():
    rfm9x.send(bytes("Team: " + TEAM_NUM + "\r\n" + "Time: " + str(int(time.monotonic())) + "\r\n", "utf-8"))
    time.sleep(.5)

# fill the ballast with water to make the float dive
def dive():
    # motor1 is the motor that fills the reservoir with water
    kit.motor1.throttle = 1.0
    time.sleep(BILGE_FILL_DURATION)
    kit.motor1.throttle = 0.0

# empty the ballast to make the float surface
def surface():
    # motor2 is the motor that empties the reservoir
    kit.motor2.throttle = 1.0
    time.sleep(BILGE_EMPTY_DURATION)
    kit.motor2.throttle = 0.0


# # # # # # # #
# Main Loop
# # # # # # # #

# wait for receive to start
while True:

    packet = rfm9x.receive()

    if packet is None:
        pass
    elif str(packet, "utf-8") == "CABRILLO VPF DIVE":
        break
    else:
        pass
        
# profiling cycle
while True:
    start_time = time.time()
    while time.time() - start_time < TRANSMIT_DURATION:
        transmit()

    dive()
    time.sleep(DIVE_DURATION)
    surface()
    time.sleep(SURFACE_DURATION)
