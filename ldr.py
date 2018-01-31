 # -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(4,GPIO.IN)
try:
    
    while True: 

        if GPIO.input(4) == 0:
            GPIO.output(17, True) ## Enciendo el 17
            time.sleep(0.2) ## Esperamos 1 segundo
            GPIO.output(17, False) ## Apago el 17
            time.sleep(0.2)
        else:
            GPIO.output(27, True) ## Enciendo el 17
            time.sleep(0.2) ## Esperamos 1 segundo
            GPIO.output(27, False) ## Apago el 17
            time.sleep(0.2)
            
            
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()

 
