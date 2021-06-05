#parcial dos seccion 2 echo por mauricio lopez el dia 18/04/2021 a las 13:56

import time
from pytictoc import TicToc
import RPi.GPIO as GPIO
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

PAHT_CRED = '/home/pi/Downloads/base-arqui2-firebase-adminsdk.json'
URL_DB = 'https://base-arqui2-default-rtdb.firebaseio.com/'
REF_registro = '/Parcial2Seccion2'

#Pines de salida
#pines display izquierdo
PinAI = 12
PinBI = 16
PinCI = 18
PinDI = 22
PinEI = 24
PinFI = 26
PinGI = 32
#pines display derecho
PinAD = 3
PinBD = 5
PinCD = 7
PinDD = 11
PinED = 13
PinFD = 15
PinGD = 19

#Pines de entrada
PinEmisor = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Setear pines
GPIO.setup(PinAI, GPIO.OUT)
GPIO.setup(PinAD, GPIO.OUT)
GPIO.setup(PinBI, GPIO.OUT)
GPIO.setup(PinBD, GPIO.OUT)
GPIO.setup(PinCI, GPIO.OUT)
GPIO.setup(PinCD, GPIO.OUT)
GPIO.setup(PinDI, GPIO.OUT)
GPIO.setup(PinDD, GPIO.OUT)
GPIO.setup(PinEI, GPIO.OUT)
GPIO.setup(PinED, GPIO.OUT)
GPIO.setup(PinFI, GPIO.OUT)
GPIO.setup(PinFD, GPIO.OUT)
GPIO.setup(PinGI, GPIO.OUT)
GPIO.setup(PinGD, GPIO.OUT)

GPIO.setup(PinEmisor, GPIO.IN)

def EscribirNumero (numero):
	Decena = numero /10
	Unidad = numero - (Decena * 10)
	
	if Unidad == 1:
		GPIO.output(PinAD, GPIO.LOW)
		GPIO.output(PinBD, GPIO.HIGH)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.LOW)
		GPIO.output(PinED, GPIO.LOW)
		GPIO.output(PinFD, GPIO.LOW)
		GPIO.output(PinGD, GPIO.LOW)
	elif Unidad == 2:
		GPIO.output(PinAD, GPIO.HIGH)
		GPIO.output(PinBD, GPIO.HIGH)
		GPIO.output(PinCD, GPIO.LOW)
		GPIO.output(PinDD, GPIO.HIGH)
		GPIO.output(PinED, GPIO.HIGH)
		GPIO.output(PinFD, GPIO.LOW)
		GPIO.output(PinGD, GPIO.HIGH)
	elif Unidad == 3:
		GPIO.output(PinAD, GPIO.HIGH)
		GPIO.output(PinBD, GPIO.HIGH)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.HIGH)
		GPIO.output(PinED, GPIO.LOW)
		GPIO.output(PinFD, GPIO.LOW)
		GPIO.output(PinGD, GPIO.HIGH)
	elif Unidad == 4:
		GPIO.output(PinAD, GPIO.LOW)
		GPIO.output(PinBD, GPIO.HIGH)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.LOW)
		GPIO.output(PinED, GPIO.LOW)
		GPIO.output(PinFD, GPIO.HIGH)
		GPIO.output(PinGD, GPIO.HIGH)
	elif Unidad == 5:
		GPIO.output(PinAD, GPIO.HIGH)
		GPIO.output(PinBD, GPIO.LOW)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.HIGH)
		GPIO.output(PinED, GPIO.LOW)
		GPIO.output(PinFD, GPIO.HIGH)
		GPIO.output(PinGD, GPIO.HIGH)
	elif Unidad == 6:
		GPIO.output(PinAD, GPIO.HIGH)
		GPIO.output(PinBD, GPIO.LOW)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.HIGH)
		GPIO.output(PinED, GPIO.HIGH)
		GPIO.output(PinFD, GPIO.HIGH)
		GPIO.output(PinGD, GPIO.HIGH)
	elif Unidad == 7:
		GPIO.output(PinAD, GPIO.HIGH)
		GPIO.output(PinBD, GPIO.HIGH)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.LOW)
		GPIO.output(PinED, GPIO.LOW)
		GPIO.output(PinFD, GPIO.LOW)
		GPIO.output(PinGD, GPIO.LOW)
	elif Unidad == 8:
		GPIO.output(PinAD, GPIO.HIGH)
		GPIO.output(PinBD, GPIO.HIGH)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.HIGH)
		GPIO.output(PinED, GPIO.HIGH)
		GPIO.output(PinFD, GPIO.HIGH)
		GPIO.output(PinGD, GPIO.HIGH)
	elif Unidad == 9:
		GPIO.output(PinAD, GPIO.HIGH)
		GPIO.output(PinBD, GPIO.HIGH)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.LOW)
		GPIO.output(PinED, GPIO.LOW)
		GPIO.output(PinFD, GPIO.HIGH)
		GPIO.output(PinGD, GPIO.HIGH)
	elif Unidad == 0:
		GPIO.output(PinAD, GPIO.HIGH)
		GPIO.output(PinBD, GPIO.HIGH)
		GPIO.output(PinCD, GPIO.HIGH)
		GPIO.output(PinDD, GPIO.HIGH)
		GPIO.output(PinED, GPIO.HIGH)
		GPIO.output(PinFD, GPIO.HIGH)
		GPIO.output(PinGD, GPIO.LOW)
		
	if Decena == 1:
		GPIO.output(PinAI, GPIO.LOW)
		GPIO.output(PinBI, GPIO.HIGH)
		GPIO.output(PinCI, GPIO.HIGH)
		GPIO.output(PinDI, GPIO.LOW)
		GPIO.output(PinEI, GPIO.LOW)
		GPIO.output(PinFI, GPIO.LOW)
		GPIO.output(PinGI, GPIO.LOW)
	elif Decena == 2:
		GPIO.output(PinAI, GPIO.HIGH)
		GPIO.output(PinBI, GPIO.HIGH)
		GPIO.output(PinCI, GPIO.LOW)
		GPIO.output(PinDI, GPIO.HIGH)
		GPIO.output(PinEI, GPIO.HIGH)
		GPIO.output(PinFI, GPIO.LOW)
		GPIO.output(PinGI, GPIO.HIGH)
	elif Decena == 3:
		GPIO.output(PinAI, GPIO.HIGH)
		GPIO.output(PinBI, GPIO.HIGH)
		GPIO.output(PinCI, GPIO.HIGH)
		GPIO.output(PinDI, GPIO.HIGH)
		GPIO.output(PinEI, GPIO.LOW)
		GPIO.output(PinFI, GPIO.LOW)
		GPIO.output(PinGI, GPIO.HIGH)
	elif Decena == 4:
		GPIO.output(PinAI, GPIO.LOW)
		GPIO.output(PinBI, GPIO.HIGH)
		GPIO.output(PinCI, GPIO.HIGH)
		GPIO.output(PinDI, GPIO.LOW)
		GPIO.output(PinEI, GPIO.LOW)
		GPIO.output(PinFI, GPIO.HIGH)
		GPIO.output(PinGI, GPIO.HIGH)
	elif Decena == 5:
		GPIO.output(PinAI, GPIO.HIGH)
		GPIO.output(PinBI, GPIO.LOW)
		GPIO.output(PinCI, GPIO.HIGH)
		GPIO.output(PinDI, GPIO.HIGH)
		GPIO.output(PinEI, GPIO.LOW)
		GPIO.output(PinFI, GPIO.HIGH)
		GPIO.output(PinGI, GPIO.HIGH)
	elif Decena == 6:
		GPIO.output(PinAI, GPIO.HIGH)
		GPIO.output(PinBI, GPIO.LOW)
		GPIO.output(PinCI, GPIO.HIGH)
		GPIO.output(PinDI, GPIO.HIGH)
		GPIO.output(PinEI, GPIO.HIGH)
		GPIO.output(PinFI, GPIO.HIGH)
		GPIO.output(PinGI, GPIO.HIGH)
	elif Decena == 7:
		GPIO.output(PinAI, GPIO.HIGH)
		GPIO.output(PinBI, GPIO.HIGH)
		GPIO.output(PinCI, GPIO.HIGH)
		GPIO.output(PinDI, GPIO.LOW)
		GPIO.output(PinEI, GPIO.LOW)
		GPIO.output(PinFI, GPIO.LOW)
		GPIO.output(PinGI, GPIO.LOW)
	elif Decena == 8:
		GPIO.output(PinAI, GPIO.HIGH)
		GPIO.output(PinBI, GPIO.HIGH)
		GPIO.output(PinCI, GPIO.HIGH)
		GPIO.output(PinDI, GPIO.HIGH)
		GPIO.output(PinEI, GPIO.HIGH)
		GPIO.output(PinFI, GPIO.HIGH)
		GPIO.output(PinGI, GPIO.HIGH)
	elif Decena == 9:
		GPIO.output(PinAI, GPIO.HIGH)
		GPIO.output(PinBI, GPIO.HIGH)
		GPIO.output(PinCI, GPIO.HIGH)
		GPIO.output(PinDI, GPIO.LOW)
		GPIO.output(PinEI, GPIO.LOW)
		GPIO.output(PinFI, GPIO.HIGH)
		GPIO.output(PinGI, GPIO.HIGH)
	elif Decena == 0:
		GPIO.output(PinAI, GPIO.LOW)
		GPIO.output(PinBI, GPIO.LOW)
		GPIO.output(PinCI, GPIO.LOW)
		GPIO.output(PinDI, GPIO.LOW)
		GPIO.output(PinEI, GPIO.LOW)
		GPIO.output(PinFI, GPIO.LOW)
		GPIO.output(PinGI, GPIO.LOW)
		
def EscribirEstado(Numero):
	if Numero == 0:
		GPIO.output(PinAI,GPIO.LOW)
		GPIO.output(PinBI,GPIO.LOW)
		GPIO.output(PinCI,GPIO.LOW)
		GPIO.output(PinDI,GPIO.HIGH)
		GPIO.output(PinEI,GPIO.HIGH)
		GPIO.output(PinFI,GPIO.HIGH)
		GPIO.output(PinGI,GPIO.LOW)
		GPIO.output(PinAD,GPIO.LOW)
		GPIO.output(PinBD,GPIO.LOW)
		GPIO.output(PinCD,GPIO.LOW)
		GPIO.output(PinDD,GPIO.LOW)
		GPIO.output(PinED,GPIO.HIGH)
		GPIO.output(PinFD,GPIO.HIGH)
		GPIO.output(PinGD,GPIO.LOW)
	elif Numero == 1:
		GPIO.output(PinAI,GPIO.LOW)
		GPIO.output(PinBI,GPIO.LOW)
		GPIO.output(PinCI,GPIO.LOW)
		GPIO.output(PinDI,GPIO.HIGH)
		GPIO.output(PinEI,GPIO.HIGH)
		GPIO.output(PinFI,GPIO.HIGH)
		GPIO.output(PinGI,GPIO.LOW)
		GPIO.output(PinAD,GPIO.HIGH)
		GPIO.output(PinBD,GPIO.HIGH)
		GPIO.output(PinCD,GPIO.HIGH)
		GPIO.output(PinDD,GPIO.HIGH)
		GPIO.output(PinED,GPIO.HIGH)
		GPIO.output(PinFD,GPIO.HIGH)
		GPIO.output(PinGD,GPIO.LOW)
	elif Numero == 2:
		GPIO.output(PinAI,GPIO.LOW)
		GPIO.output(PinBI,GPIO.HIGH)
		GPIO.output(PinCI,GPIO.HIGH)
		GPIO.output(PinDI,GPIO.LOW)
		GPIO.output(PinEI,GPIO.HIGH)
		GPIO.output(PinFI,GPIO.HIGH)
		GPIO.output(PinGI,GPIO.HIGH)
		GPIO.output(PinAD,GPIO.HIGH)
		GPIO.output(PinBD,GPIO.HIGH)
		GPIO.output(PinCD,GPIO.HIGH)
		GPIO.output(PinDD,GPIO.LOW)
		GPIO.output(PinED,GPIO.HIGH)
		GPIO.output(PinFD,GPIO.HIGH)
		GPIO.output(PinGD,GPIO.HIGH)
	elif Numero == 3:
		GPIO.output(PinAI,GPIO.LOW)
		GPIO.output(PinBI,GPIO.HIGH)
		GPIO.output(PinCI,GPIO.HIGH)
		GPIO.output(PinDI,GPIO.LOW)
		GPIO.output(PinEI,GPIO.HIGH)
		GPIO.output(PinFI,GPIO.HIGH)
		GPIO.output(PinGI,GPIO.HIGH)
		GPIO.output(PinAD,GPIO.LOW)
		GPIO.output(PinBD,GPIO.LOW)
		GPIO.output(PinCD,GPIO.LOW)
		GPIO.output(PinDD,GPIO.LOW)
		GPIO.output(PinED,GPIO.HIGH)
		GPIO.output(PinFD,GPIO.HIGH)
		GPIO.output(PinGD,GPIO.LOW)


def ProyeccionTrafico(niveltrafico, cantidadcarros):
	if cantidadcarros  == 0:
		return 0
	else:
		return cantidadcarros / niveltrafico
	
	
def CalNivelTrafico(carros):
	if carros > 10:
		return 3
	elif carros > 7:
		return 2
	elif carros > 0:
		return 1
	else:
		return 0
	
	
	
	
	
	
t = TicToc()
contador1 = 0
contador2 = 0
while True:
	t.tic()
	contador2 = 0
	while t.tocvalue() < 15:
		if GPIO.input(PinEmisor) == GPIO.LOW:
			contador2 = contador2 + 1
			time.sleep(0.5)
	NivelTrafico = CalNivelTrafico(contador2)
	contador1 = contador1 + contador2
	print("Registro")
	print("Numero de carros: " + str(contador1))
	if NivelTrafico == 0:
		print("Libre")
	elif NivelTrafico == 1:
		print("Bajo")
	elif NivelTrafico == 2:
		print("Normal")
	elif NivelTrafico == 3:
		print("Alto")
	EscribirNumero(contador1)
	time.sleep(5)
	EscribirEstado(NivelTrafico)
	time.sleep(5)
	EscribirNumero(ProyeccionTrafico(NivelTrafico, contador2))
