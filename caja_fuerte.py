  # -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time  
import random
import os
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

num = random.randrange(1,10,1)


def funcion():
    cont = 0
    vidas = 3
    i = 0  
    lista = []
  #  print(num)
   # print(len(lista))
#   if len(lista) == 0:
  #      print (cont)
       # for x in range(len(lista)):
 #   time.sleep(0.2)
#num_leds = 10 - num
 #   for i in range(num_leds):
   #     GPIO.output(14, True)
    #  time.sleep(0.2)
     #   GPIO.output(14, False)
      # time.sleep(0.2)
       #GPIO.output(15, True)
        #time.sleep(0.2)
        #GPIO.output(15, False)
        #time.sleep(0.2)
        
    print("Introduce un numero con el pulsador izquierdo")
    try:
        while vidas >= 0:
            input_state2 = GPIO.input(27)
            input_state1 = GPIO.input(17)
            input_state  = GPIO.input(4)
            if input_state == False:
                os.system('clear')    
                time.sleep(0.3)
                GPIO.output(15, True)
                time.sleep(0.1)
                GPIO.output(15, False)
                time.sleep(0.1)
                cont = cont + 1
            
                if len(lista) == 0:
                    if cont > 10:
                        cont = 1
                        print(cont)
                    else:
                        print(cont)
                    
                else:
        
                        
                        for x in range(len(lista)):
                            if cont > 10:
                                cont = 1
                                
                            if lista[x] == cont:
                                if lista[x] == 10:
                                    cont = 1
                                else:
                                    cont = cont + 1
                                    
                                                           
                            
                        print(cont)
                                
            if input_state2 == False:
                os.system('clear')    
                time.sleep(0.3)
                GPIO.output(14, True)
                time.sleep(0.1)
                GPIO.output(14, False)
                time.sleep(0.1)
                cont = cont - 1
            
                if len(lista) == 0:
                                        
                    if cont <= 0:
                        cont = 10
                        print(cont)
                    else:
                        print(cont)
                    
                
                    
                else:
        
                        
                        for x in range(len(lista)):
                            
                            
                            if cont <= 0:
                                cont = 10
                                
                        
                                
                            if lista[x] == cont:
                                if lista[x] == 1:
                                    cont = 10
                                else:
                                    cont = cont - 1
                                    
                        print(cont)
                          
            if input_state1 == False:
                time.sleep(0.3)  
                if cont == num:
                    print("Perfecto!!!")
                    GPIO.output(15, True)
                    time.sleep(0.1)
                    GPIO.output(15, False)
                    time.sleep(0.1)
                    GPIO.output(15, True)
                    time.sleep(0.1)
                    GPIO.output(15, False)
                    time.sleep(0.1)
                    GPIO.output(15, True)
                    time.sleep(0.1)
                    GPIO.output(15, False)
                    break
                
                if cont != num and vidas >= 0:
                    vidas = vidas - 1
                    if vidas == 0:
                        print("No has acertado")
                        print(lista)
                        GPIO.output(14, True)
                        GPIO.output(15,True)
                        time.sleep(5)
                        GPIO.output(14, False)
                        GPIO.output(15, False)
                        
                        break
                    else:
                    
                        lista.insert(i, cont)
                        i = i + 1
                        cont = 0
                        GPIO.output(14, True)
                        time.sleep(0.1)
                        GPIO.output(14, False)
                        time.sleep(0.1)
                        GPIO.output(14, True)
                        time.sleep(0.1)
                        GPIO.output(14, False)
                        time.sleep(0.1)
                        GPIO.output(14, True)
                        time.sleep(0.1)
                        GPIO.output(14, False)
                        
                        print("No has acertado. Te quedan " + str(vidas) + " vidas")
                        continue
    except KeyboardInterrupt:
        GPIO.cleanup()
funcion()
GPIO.cleanup()
print("Juego acabado")
#print("El numero era el " + str(num))

    
