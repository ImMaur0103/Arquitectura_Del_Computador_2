#ejemplo hecho en clase el dia 24/03/2021

import RPi.GPIO as GPIO
import time

print ("hola")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)

def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(2)
        GPIO.output(pin,GPIO.LOW)
        time.sleep(0.5)
        return

for i in range(0,50):
        blink(7)
        
GPIO.cleanup()

