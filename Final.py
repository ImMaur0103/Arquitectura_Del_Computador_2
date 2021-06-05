#Examen final

from pytictoc import TicToc
import RPi.GPIO as GPIO
import time


#Asignar pines
PinControlar = 12
PinB = 40

#Inicializar Rasp y sus pines
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#Setear pines
GPIO.setup(PinControlar, GPIO.OUT)
GPIO.setup(PinB, GPIO.OUT)


def CambioAMorse(Numero):
	if Numero == '0':
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
	elif Numero == '1':
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
	elif Numero == '2':
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
	elif Numero == '3':
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
	elif Numero == '4':
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
	elif Numero == '5':
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
	elif Numero == '6':
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
	elif Numero == '7':
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
	elif Numero == '8':
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)
	elif Numero == '9':
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.HIGH)
		time.sleep(2)
		GPIO.output(PinControlar,GPIO.LOW)
		time.sleep(2)


GPIO.output(PinControlar,GPIO.HIGH)
GPIO.output(PinB,GPIO.LOW)
while True:
	variable = input()
	if len(str(variable)) == 10:
		time.sleep(10)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[0])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[1])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[2])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[3])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[4])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[5])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[6])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[7])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[8])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		GPIO.output(PinB,GPIO.HIGH)
		CambioAMorse(str(variable)[9])
		GPIO.output(PinB,GPIO.LOW)
		time.sleep(5)
		
		
		
		
		
		
		
		
		
		
