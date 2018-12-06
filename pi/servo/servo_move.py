# https://tutorials-raspberrypi.com/raspberry-pi-servo-motor-control/
#
# The period is 20ms long.
# In addition, a duty cycle of between 5% and 10% of the period is expected.
# Thus the pulse duration is between 1ms and 2ms. Usually, servos can rotate
# between 0 and 180. So we have to adjust the pulse length in between.
# A length of 1.5ms (7.5%) thus gives an angle of 90. And all at precisely 50x per second (50Hz).


import RPi.GPIO as GPIO
import time
import sys

servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

SLEEP_TIME=1.2

angle=0
if len(sys.argv)>=2:
  angle=int(sys.argv[1])

dc = 2.5 + 10 * (180 - angle) / 180
#print(dc)
try:
  p.ChangeDutyCycle(dc)
  time.sleep(SLEEP_TIME)
  p.stop()
  GPIO.cleanup()
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()
