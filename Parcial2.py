#Parcial 2
import time
import RPi.GPIO as GPIO
from datetime import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

PAHT_CRED = '/home/pi/Downloads/base-arqui2-firebase-adminsdk.json'
URL_DB = 'https://base-arqui2-default-rtdb.firebaseio.com/'
REF_registro = '/Registro'
#Pines de salida
PinAgua = 12
PinShampo = 16
PinRodillos = 18
PinEscobas = 22
PinSecado = 24
PinFin = 19
PinCarroActivo = 40
#Pines de entrada
PinCP = 3
PinCM = 5
PinCG = 7
PinCarro = 11

#Configuracion pines
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PinAgua, GPIO.OUT)
GPIO.setup(PinShampo, GPIO.OUT)
GPIO.setup(PinRodillos, GPIO.OUT)
GPIO.setup(PinEscobas, GPIO.OUT)
GPIO.setup(PinSecado, GPIO.OUT)
GPIO.setup(PinFin, GPIO.OUT)
GPIO.setup(PinCarroActivo, GPIO.OUT)
GPIO.setup(PinCP, GPIO.IN)
GPIO.setup(PinCM, GPIO.IN)
GPIO.setup(PinCG, GPIO.IN)
GPIO.setup(PinCarro, GPIO.IN)

#Credenciales Base de datos
cred = credentials.Certificate(PAHT_CRED)
firebase_admin.initialize_app(cred, {
	'databaseURL': URL_DB
})

Ref_in = db.reference(REF_registro)



def ProcesoCarro():
	Entrada = datetime.now()
	tiempo = 0
	Carro = 0
	tipocarro = ""
	if GPIO.input(PinCP) == GPIO.HIGH:
		Carro = 1
		tipocarro = "Small"
		print("	the car is small")
	elif GPIO.input(PinCM) == GPIO.HIGH:
		Carro = 2
		tipocarro = "Medium"
		print("	the car is medium")
	elif GPIO.input(PinCG) == GPIO.HIGH:
		Carro = 3
		tipocarro = "Large"
		print("	the car is large")
		
	print("Water cicle")
	GPIO.output(PinAgua, GPIO.HIGH)
	if Carro == 1:
		time.sleep(2)
		tiempo = tiempo + 2
	elif Carro == 2:
		time.sleep(4)
		tiempo = tiempo + 4
	elif Carro == 3:
		time.sleep(6)
		tiempo = tiempo + 6
	GPIO.output(PinAgua, GPIO.LOW)
	
	print("Shampoo cicle")
	GPIO.output(PinShampo, GPIO.HIGH)
	if Carro == 1:
		time.sleep(3)
		tiempo = tiempo + 3
	elif Carro == 2:
		time.sleep(6)
		tiempo = tiempo + 6
	elif Carro == 3:
		time.sleep(9)
		tiempo = tiempo + 9
	GPIO.output(PinShampo, GPIO.LOW)
		
	print("cleaning rollers cicle")
	GPIO.output(PinRodillos, GPIO.HIGH)
	if Carro == 1:
		time.sleep(3)
		tiempo = tiempo + 3
	elif Carro == 2:
		time.sleep(6)
		tiempo = tiempo + 6
	elif Carro == 3:
		time.sleep(9)
		tiempo = tiempo + 9
	GPIO.output(PinRodillos, GPIO.LOW)
		
	print("cleaning brooms cicle")
	GPIO.output(PinEscobas, GPIO.HIGH)
	if Carro == 1:
		time.sleep(3)
		tiempo = tiempo + 3
	elif Carro == 2:
		time.sleep(6)
		tiempo = tiempo + 6
	elif Carro == 3:
		time.sleep(9)
		tiempo = tiempo + 9
	GPIO.output(PinEscobas, GPIO.LOW)
		
	print("Water cicle")
	GPIO.output(PinAgua, GPIO.HIGH)
	if Carro == 1:
		time.sleep(2)
		tiempo = tiempo + 2
	elif Carro == 2:
		time.sleep(4)
		tiempo = tiempo + 4
	elif Carro == 3:
		time.sleep(6)
		tiempo = tiempo + 6
	GPIO.output(PinAgua, GPIO.LOW)
		
	print("drying cicle")
	GPIO.output(PinSecado, GPIO.HIGH)
	if Carro == 1:
		time.sleep(5)
		tiempo = tiempo + 5
	elif Carro == 2:
		time.sleep(7)
		tiempo = tiempo + 7
	elif Carro == 3:
		time.sleep(10)
		tiempo = tiempo + 10
	GPIO.output(PinSecado, GPIO.LOW)
	
	Salida = datetime.now()
	
	precio = tiempo * 2
	precio = precio * Carro
	Ref_in.push({
	"Fecha y hora de entrada": Entrada.strftime("%m/%d/%Y, %H:%M:%S"),
	"Fecha y hora de salida": Salida.strftime("%m/%d/%Y, %H:%M:%S"),
	"Precio": precio,
	"Tiempo dentro":tiempo,
	"Tipo": tipocarro
	})
	GPIO.output(PinFin, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(PinFin, GPIO.LOW)
	
	
	

while True:
	tiempoespera = 0
	if GPIO.input(PinCarro) == GPIO.LOW:
		#Llego carro
		print("Enter a Car")
		GPIO.output(PinCarroActivo, GPIO.HIGH)
		ProcesoCarro()
		GPIO.output(PinCarroActivo, GPIO.LOW)
	print("")
	print("Waiting")
	print("")
	while GPIO.input(PinCarro) == GPIO.HIGH:
		tiempoespera = tiempoespera + 1








