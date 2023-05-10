# Cabrillo Robotics Club
# Vertical Profiling Float
# Float

# python hardware interfaces
import board
import busio
import digitalio
import os

# lora radio library
import adafruit_rfm9x

import time

# gps wing library
import adafruit_gps

# get board details
board_type = os.uname().machine

# instantiate the spi interface
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

# instanciate uart interface
uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=10)


#
# LoRa Radio Wing SETUP
#

# set the Chip Select and Reset pins based on board type
if "Particle Xenon" in board_type:
    CS = digitalio.DigitalInOut(board.D2)
    RESET = digitalio.DigitalInOut(board.D3)
elif "RFM9x" in board_type:
    CS = digitalio.DigitalInOut(board.RFM9X_CS)
    RESET = digitalio.DigitalInOut(board.RFM9X_RST)
else:
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

#
# gps wing setup
#

# instanciate the gps object
gps = adafruit_gps.GPS(uart, debug=False)

# enable all features
gps.send_command(b'PMTK314,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set update rate to every half second
gps.send_command(b"PMTK220,500")



while True:

    rfm9x.send(bytes("Message 1\r\n", "utf-8"))

    time.sleep(5)

    rfm9x.send(bytes("Message 2\r\n", "utf-8"))

    time.sleep(5)
