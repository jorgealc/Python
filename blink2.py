import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 omo salida
GPIO.setup(4, GPIO.OUT) ## GPIO 4 como salida
GPIO.output(17, True)
def blink():
        try:
                
                print "Ejecucion iniciada..."
                iteracion = 0
                while iteracion < 30: ## Segundos que durara la funcion
                        GPIO.output(17, True) ## Enciendo el 17
                        GPIO.output(4, False) ## Apago el 27
                        time.sleep(5) ## Esperamos 1 segundo
                        GPIO.output(17, False) ## Apago el 17
                        GPIO.output(4, True) ## Enciendo el 27
                        time.sleep(1) ## Esperamos 1 segundo
                        iteracion = iteracion + 2 ## Sumo 2 porque he hecho dos parpadeos
                print "Ejecucion finalizada"
                GPIO.cleanup() ## Hago una limpieza de los GPIO
        except KeyboardInterrupt:
                GPIO.cleanup()
blink() ## Hago la llamada a la funcion blink
