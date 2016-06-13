import RPi.GPIO as GPIO
import time
import picamera

SENSOR = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN) #Sensors 18 is input
CAMERA = picamera.PiCamera()
imagenumber = 0

while True:
    i = GPIO.input(SENSOR)
    if i == 0: #sensor is not active
        print "Nuthing to see",i
        time.sleep (0.1)

    elif i==1: #When sensor detects something
        CAMERA.capture('sensorImage' + str(imagenumber) + '.jpg')
        print "Captured image number" + str(imagenumber)
        if imagenumber >= 20:
            imagenumber = 0
        else:
            imagenumber += 1
        time.sleep (0.1)

GPIO.cleanup ()
