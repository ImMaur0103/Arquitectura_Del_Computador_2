#laboratorio 9

from pytictoc import TicToc
import RPi.GPIO as GPIO
import requests
import math

#pines display
PinA = 3
PinB = 5
PinC = 7
PinD = 11
PinE = 13
PinF = 15
PinG = 19
PinH = 40

#Pines de entrada
Pinboton = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Setear pines
GPIO.setup(PinA, GPIO.OUT)
GPIO.setup(PinB, GPIO.OUT)
GPIO.setup(PinC, GPIO.OUT)
GPIO.setup(PinD, GPIO.OUT)
GPIO.setup(PinE, GPIO.OUT)
GPIO.setup(PinF, GPIO.OUT)
GPIO.setup(PinG, GPIO.OUT)
GPIO.setup(PinH, GPIO.OUT)
GPIO.setup(Pinboton, GPIO.IN)

def encender(Pin, Bool):
	if Bool:
		GPIO.output(Pin, GPIO.HIGH)
	else:
		GPIO.output(Pin, GPIO.LOW)

def EscribirNumero (numero):
	if numero[1] == '1':
		encender(PinA, True)
	else:
		encender(PinA, False)
		
	if numero[2] == '1':
		encender(PinB, True)
	else:
		encender(PinB, False)
		
	if numero[3] == '1':
		encender(PinC, True)
	else:
		encender(PinC, False)
		
	if numero[4] == '1':
		encender(PinD, True)
	else:
		encender(PinD, False)
		
	if numero[5] == '1':
		encender(PinE, True)
	else:
		encender(PinE, False)
		
	if numero[6] == '1':
		encender(PinF, True)
	else:
		encender(PinF, False)
		
	if numero[7] == '1':
		encender(PinG, True)
	else:
		encender(PinG, False)
		
	if numero[8] == '1':
		encender(40, True)
	else:
		encender(40, False)
		
GPIO.output(PinH,GPIO.HIGH)
GPIO.output(PinH,GPIO.LOW)
T = TicToc()
url = 'https://vqfyr7aom6.execute-api.us-east-2.amazonaws.com/V1'
urlcomplemento = '?time='
while True:
	if GPIO.input(Pinboton) == GPIO.LOW:
		print('entro')
		T.tic()
		while True:
			if GPIO.input(Pinboton) == GPIO.HIGH:
				break
		string = (url + urlcomplemento + "{:.0f}".format(T.tocvalue()))
		if GPIO.input(40) == GPIO.HIGH:
			string += '1'
		else:
			string += '2'
		print(string)
		r = requests.post(string)
		obtenido = r.text
		print(obtenido)
		EscribirNumero(obtenido)
			

