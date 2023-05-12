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

# python hardware interfaces
import board
import busio
import digitalio
import os

# lora radio library
import adafruit_rfm9x

import time

# instantiate the spi interface
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

#
# LoRa Radio Wing SETUP
#

CS = digitalio.DigitalInOut(board.D5)
RESET = digitalio.DigitalInOut(board.D6)

# set the radio frequency to 915mhz
RADIO_FREQ_MHZ = 915.0 

# instantiate the lora radio in 915mhz mode
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

# set my lora node ID
rfm9x.node = 100

# set the destination lora node ID
# destination is deck
rfm9x.destination = 50

while True:

    rfm9x.send(bytes("Team: PN01" + "\r\n" + "Time: " + str(int(time.monotonic())) + "\r\n", "utf-8"))

    time.sleep(.5)