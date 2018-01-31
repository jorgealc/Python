# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time    

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT )
GPIO.setup(27, GPIO.OUT )

cont = 0 
try:
    
    while True: 
        
        input_state = GPIO.input(4)
        if input_state == False:
            
            GPIO.output(17, True)      # Enciende el LED
            GPIO.output(27, False)
            cont = cont + 1
            time.sleep(0.3)
            print(cont)  
           # print('Botón pulsado')
        #    time.sleep(5)
        #    GPIO.output(17, False)     # Apaga el LED
        if input_state == 1:
            GPIO.output(17, False)
            GPIO.output(27, True)
            
            
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    print(cont)
    GPIO.cleanup()   
