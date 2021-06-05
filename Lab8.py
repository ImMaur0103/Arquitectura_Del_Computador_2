#Laboratorio 8
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
GPIO.setup(Pinboton, GPIO.IN)

def EscribirNumero (numero):
	if numero == '"uno"':
		GPIO.output(PinA, GPIO.LOW)
		GPIO.output(PinB, GPIO.HIGH)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.LOW)
		GPIO.output(PinE, GPIO.LOW)
		GPIO.output(PinF, GPIO.LOW)
		GPIO.output(PinG, GPIO.LOW)
	elif numero == '"dos"':
		GPIO.output(PinA, GPIO.HIGH)
		GPIO.output(PinB, GPIO.HIGH)
		GPIO.output(PinC, GPIO.LOW)
		GPIO.output(PinD, GPIO.HIGH)
		GPIO.output(PinE, GPIO.HIGH)
		GPIO.output(PinF, GPIO.LOW)
		GPIO.output(PinG, GPIO.HIGH)
	elif numero == '"tres"':
		GPIO.output(PinA, GPIO.HIGH)
		GPIO.output(PinB, GPIO.HIGH)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.HIGH)
		GPIO.output(PinE, GPIO.LOW)
		GPIO.output(PinF, GPIO.LOW)
		GPIO.output(PinG, GPIO.HIGH)
	elif numero == '"cuatro"':
		GPIO.output(PinA, GPIO.LOW)
		GPIO.output(PinB, GPIO.HIGH)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.LOW)
		GPIO.output(PinE, GPIO.LOW)
		GPIO.output(PinF, GPIO.HIGH)
		GPIO.output(PinG, GPIO.HIGH)
	elif numero == '"cinco"':
		GPIO.output(PinA, GPIO.HIGH)
		GPIO.output(PinB, GPIO.LOW)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.HIGH)
		GPIO.output(PinE, GPIO.LOW)
		GPIO.output(PinF, GPIO.HIGH)
		GPIO.output(PinG, GPIO.HIGH)
	elif numero == '"seis"':
		GPIO.output(PinA, GPIO.HIGH)
		GPIO.output(PinB, GPIO.LOW)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.HIGH)
		GPIO.output(PinE, GPIO.HIGH)
		GPIO.output(PinF, GPIO.HIGH)
		GPIO.output(PinG, GPIO.HIGH)
	elif numero == '"siete"':
		GPIO.output(PinA, GPIO.HIGH)
		GPIO.output(PinB, GPIO.HIGH)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.LOW)
		GPIO.output(PinE, GPIO.LOW)
		GPIO.output(PinF, GPIO.LOW)
		GPIO.output(PinG, GPIO.LOW)
	elif numero == '"ocho"':
		GPIO.output(PinA, GPIO.HIGH)
		GPIO.output(PinB, GPIO.HIGH)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.HIGH)
		GPIO.output(PinE, GPIO.HIGH)
		GPIO.output(PinF, GPIO.HIGH)
		GPIO.output(PinG, GPIO.HIGH)
	elif numero == '"nueve"':
		GPIO.output(PinA, GPIO.HIGH)
		GPIO.output(PinB, GPIO.HIGH)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.LOW)
		GPIO.output(PinE, GPIO.LOW)
		GPIO.output(PinF, GPIO.HIGH)
		GPIO.output(PinG, GPIO.HIGH)
	elif numero == '"cero"':
		GPIO.output(PinA, GPIO.HIGH)
		GPIO.output(PinB, GPIO.HIGH)
		GPIO.output(PinC, GPIO.HIGH)
		GPIO.output(PinD, GPIO.HIGH)
		GPIO.output(PinE, GPIO.HIGH)
		GPIO.output(PinF, GPIO.HIGH)
		GPIO.output(PinG, GPIO.LOW)
		
T = TicToc()
url = 'https://vqfyr7aom6.execute-api.us-east-2.amazonaws.com/V1'
urlcomplemento = '?time='
while True:
	if GPIO.input(Pinboton) == GPIO.LOW:
		T.tic()
		while True:
			if GPIO.input(Pinboton) == GPIO.HIGH:
				break
		r = requests.post(url + urlcomplemento + "{:.0f}".format(T.tocvalue()))
		obtenido = r.text
		print(obtenido)
		EscribirNumero(obtenido)
			
