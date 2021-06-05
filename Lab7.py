#Laboratorio 7 Arquitectura del computador 2
#Emisor y receptor con base de datos

import time
import RPi.GPIO as GPIO
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

PAHT_CRED = '/home/pi/Downloads/base-arqui2-firebase-adminsdk.json'
URL_DB = 'https://base-arqui2-default-rtdb.firebaseio.com/'
REF_Interrupcion = '/Interrupcion'
REF_Continuidad = '/Continuidad'
PinEmisor = 16
PinLed = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PinEmisor, GPIO.IN)
GPIO.setup(PinLed, GPIO.OUT)

cred = credentials.Certificate(PAHT_CRED)
firebase_admin.initialize_app(cred, {
	'databaseURL': URL_DB
})


Ref_in = db.reference(REF_Interrupcion)
Ref_con = db.reference(REF_Continuidad)

while True:
	tiempo = datetime.now()
	if GPIO.input(PinEmisor) == GPIO.LOW:
		GPIO.output(PinLed, GPIO.HIGH)
		print('Se detecto una interrupcion')
		print(tiempo)
		Ref_in.push({
		"Fecha y hora": tiempo.strftime("%m/%d/%Y, %H:%M:%S")
		})
		while True:
			if GPIO.input(PinEmisor) == GPIO.HIGH:
				break 
	elif GPIO.input(PinEmisor) == GPIO.HIGH:
		GPIO.output(PinLed, GPIO.LOW)
		print('se detecto una continuidad')
		print(tiempo)
		Ref_con.push({
		"Fecha y hora": tiempo.strftime("%m/%d/%Y, %H:%M:%S")
		})
		while True:
			if GPIO.input(PinEmisor) == GPIO.LOW:
				break 
		
	time.sleep(0.5)


GPIO.cleanup()
