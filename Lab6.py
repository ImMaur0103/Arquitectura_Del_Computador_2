#laboratorio 6 arquitectura del computador 2
#Receptor y emisor con raspberry
import sys
import signal
from threading import Thread
import RPi.GPIO as GPIO
import time
from datetime import datetime

tiempo = datetime.now()
PinEmisor = 3
PinLed = 5

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PinEmisor, GPIO.IN)
GPIO.setup(PinLed, GPIO.OUT)


while True:
	tiempo = datetime.now()
	if GPIO.input(PinEmisor) == GPIO.LOW:
		GPIO.output(PinLed, GPIO.HIGH)
		print('Se detecto una interrupcion')
		print(tiempo)
		while True:
			if GPIO.input(PinEmisor) == GPIO.HIGH:
				break 
	elif GPIO.input(PinEmisor) == GPIO.HIGH:
		GPIO.output(PinLed, GPIO.LOW)
		print('se detecto una continuidad')
		print(tiempo)
		while True:
			if GPIO.input(PinEmisor) == GPIO.LOW:
				break


GPIO.cleanup()
