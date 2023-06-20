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

# Function to control the motors
def run_motors(motor1_duration, motor2_duration):
    kit.motor1.throttle = 1.0  # Run motor 1 at full speed
    time.sleep(motor1_duration)  # Run motor 1 for the specified duration
    kit.motor1.throttle = 0.0  # Stop motor 1
    time.sleep(5)
    kit.motor2.throttle = 1.0  # Run motor 2 at full speed
    time.sleep(motor2_duration)  # Run motor 2 for the specified duration
    kit.motor2.throttle = 0.0  # Stop motor 2

# Main program loop
while True:
    motor1_duration = 3  # Duration to run motor 1 (in seconds)
    motor2_duration = 3  # Duration to run motor 2 (in seconds)

    run_motors(motor1_duration, motor2_duration)

    # Delay between cycles
    time.sleep(5)
