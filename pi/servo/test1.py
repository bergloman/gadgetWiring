# pin 11 is 6th in the left column (to orange wire of the motor)
# gnd is 5th in the left column (to brown wire of the motor)
# 5V is 1st in the right column (to red wire of the motor)

import RPi.GPIO as GPIO
import time

pin_val = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_val, GPIO.OUT)

try:
    while True:
        GPIO.output(pin_val, 1)
        time.sleep(0.0015)
        GPIO.output(pin_val, 0)
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
