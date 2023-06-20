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

import time
import board
import digitalio
from adafruit_motorkit import MotorKit

# Set up the motor kit
kit = MotorKit()

# descend function
def descend():
    # motor1 is the motor that fills the reservoir with water
    kit.motor1.throttle = 1.0  
    time.sleep(5) 
    kit.motor1.throttle = 0.0  
    time.sleep(5)

# ascend function
def ascend():
    kit.motor2.throttle = 1.0 
    time.sleep(5) 
    kit.motor2.throttle = 0.0  
    time.sleep(5)

# Main program loop
while True:
    descend()
    ascend()

    time.sleep(5)
