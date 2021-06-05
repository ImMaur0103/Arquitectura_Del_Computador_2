#ejemplo hecho en clase el dia 24/03/2021

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.IN)

while True:
	if GPIO.input(11):
		GPIO.output(7, GPIO.LOW)
	else:
		GPIO.output(7,GPIO.HIGH)
