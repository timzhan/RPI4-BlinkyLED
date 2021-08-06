######################################################################################
# This sample is written to test blinky LED 
# with an led connnected to Raspberry Pi 4B
# by tz
######################################################################################

import RPi.GPIO as gpio
import time


# Configure the PIN connected to the LED
pin = 4
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.OUT)
gpio.setwarnings(False)

# Configure Blinking interval value in seconds
interval = 0.5

# Led blinks 5 times
times = 5
for i in range(0, times):
    gpio.output(pin, gpio.HIGH)
    time.sleep(interval)
    gpio.output(pin, gpio.LOW)
    time.sleep(interval)

# Release the resource
gpio.cleanup()
