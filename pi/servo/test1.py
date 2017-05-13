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
