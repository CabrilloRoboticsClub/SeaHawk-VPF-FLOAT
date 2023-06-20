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

# team number as defined by MATE
TEAM_NUM = "PN03"

# chip select pin
CS = digitalio.DigitalInOut(board.D5)

# reset pin
RESET = digitalio.DigitalInOut(board.D6)

# LoRa Frequency 915mhz (NOT 800)
RADIO_FREQ_MHZ = 915.0 

import time
import board
import busio
import digitalio

# motor kit for the water pumps
from adafruit_motorkit import MotorKit

# lora radio library
import adafruit_rfm9x

import time

# instantiate the spi interface
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

#
# LoRa Radio Wing SETUP
#

# instantiate the lora radio in 915mhz mode
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# set my lora node ID
rfm9x.node = 18

# set the destination lora node ID
# destination is deck
rfm9x.destination = 28

# Set up the motor kit
kit = MotorKit()


duration = 10
start_time = time.time()
def transmit():
    rfm9x.send(bytes("Team: " + TEAM_NUM + "\r\n" + "Time: " + str(int(time.monotonic())) + "\r\n", "utf-8"))
    time.sleep(.5)

# descend function
def descend():
    # motor1 is the motor that fills the reservoir with water
    kit.motor1.throttle = 1.0  
    time.sleep(5) 
    kit.motor1.throttle = 0.0  

# ascend function
def ascend():
    # motor2 is the motor that empties the reservoir
    kit.motor2.throttle = 1.0 
    time.sleep(5) 
    kit.motor2.throttle = 0.0  

# Main program loop
while True:
    while time.time() - start_time < duration:
        transmit()

    descend()
    time.sleep(5)
    ascend()
    time.sleep(5)
