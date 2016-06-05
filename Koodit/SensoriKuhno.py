import RPi.GPIO as GPIO
import time
 
LED = 4
SENSOR = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN) #Sensors 18 is input
GPIO.setup(LED, GPIO.OUT)  #LED 4 is output
 
while True:
    i = GPIO.input(SENSOR)
    if i == 0: #sensor is not active
        print "Where are you?",i
        GPIO.output (LED,0) #LED is off
        time.sleep (0.1)
 
    elif i==1: #When sensor detects something
        print "There you are!",i
        GPIO.output (LED, 1)#Turn led on!
        time.sleep (0.1)
 
GPIO.cleanup ()
