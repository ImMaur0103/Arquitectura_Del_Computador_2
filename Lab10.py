#Laboratorio 10 y laboratorio extra

from pytictoc import TicToc
import RPi.GPIO as GPIO
import requests
import time

#Pine de Salida
PinA = 3
PinB = 5
PinC = 7
PinD = 11
PinE = 13
PinF = 15
PinG = 19
PinAI = 12
PinBI = 16
PinR = 18
Pininicio = 22
#Pines de Entrada
Pinboton = 40
PinDip1 = 26
PinDip2 = 32
PinDip3 = 36
PinDip4 = 38

#Inicializar Rasp y sus pines
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
GPIO.setup(PinAI, GPIO.OUT)
GPIO.setup(PinBI, GPIO.OUT)
GPIO.setup(PinR, GPIO.OUT)
GPIO.setup(Pininicio, GPIO.OUT)
GPIO.setup(Pinboton, GPIO.IN)
GPIO.setup(PinDip1, GPIO.IN)
GPIO.setup(PinDip2, GPIO.IN)
GPIO.setup(PinDip3, GPIO.IN)
GPIO.setup(PinDip4, GPIO.IN)

GPIO.output(Pininicio, GPIO.HIGH)
time.sleep(5)

def encenderapagar(contador):
	for i in range(contador):
		GPIO.output(PinR, GPIO.HIGH)
		time.sleep(0.5)
		GPIO.output(PinR, GPIO.LOW)
		time.sleep(0.5)
def encender(Pin, Bool):
	if Bool:
		GPIO.output(Pin, GPIO.HIGH)
	else:
		GPIO.output(Pin, GPIO.LOW)
def EscribirNumero (numero):
	if numero[0] == '1':
		encender(PinA, True)
	else:
		encender(PinA, False)
		
	if numero[1] == '1':
		encender(PinB, True)
	else:
		encender(PinB, False)
		
	if numero[2] == '1':
		encender(PinC, True)
	else:
		encender(PinC, False)
		
	if numero[3] == '1':
		encender(PinD, True)
	else:
		encender(PinD, False)
		
	if numero[4] == '1':
		encender(PinE, True)
	else:
		encender(PinE, False)
		
	if numero[5] == '1':
		encender(PinF, True)
	else:
		encender(PinF, False)
		
	if numero[6] == '1':
		encender(PinG, True)
	else:
		encender(PinG, False)
		
	if numero[7] == '1':
		encender(PinAI, True)
		encender(PinBI, True)
	else:
		encender(PinAI, False)
		encender(PinBI, False)
		
	if numero[8] != "'":
		Numero = numero[8]
		if numero[9] != "'":
			Numero += numero[9]
		encenderapagar(int(Numero))
		
#
GPIO.output(Pininicio, GPIO.LOW)

while True:
	url = 'https://vqfyr7aom6.execute-api.us-east-2.amazonaws.com/V1/'
	urlcomplemento = '?presiono='
	while GPIO.input(Pinboton) == GPIO.HIGH:
		enviar = ""
		if GPIO.input(PinDip1) == GPIO.HIGH:
			enviar += '1'
		else:
			enviar += '0'
		if GPIO.input(PinDip2) == GPIO.HIGH:
			enviar += '1'
		else:
			enviar += '0'
		if GPIO.input(PinDip3) == GPIO.HIGH:
			enviar += '1'
		else:
			enviar += '0'
		if GPIO.input(PinDip4) == GPIO.HIGH:
			enviar += '1'
		else:
			enviar += '0'
		r = requests.get(url + urlcomplemento + "RW" + enviar)
		print r.text
		r = requests.get(url + urlcomplemento +"L")
		while r.text[3] == enviar[0] and r.text[4] == enviar[1] and r.text[5] == enviar[2] and r.text[6] == enviar[3] and r.text[7] == "'":
			r = requests.get(url + urlcomplemento + "L")
		r = requests.get(url + urlcomplemento + "RR")
		print (r.text)
		EscribirNumero(r.text[3] + r.text[4] + r.text[5] + r.text[6] + r.text[7] + r.text[8] + r.text[9] + r.text[10] + r.text[11] + r.text[12])
	


