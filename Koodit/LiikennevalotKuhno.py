import RPi.GPIO as GPIO
import time
 
#Pedestrial lights m = mark, g = green, r = red
PEDM = 26
PEDG = 27
PEDR = 4
#Button
PAINIKE = 19
#Car lights: g = green, y = yellow, r = red
CARG = 23
CARY = 24
CARR = 25
#Car sensor
SENSOR = 18
 
#Setting inputs and outputs
GPIO.setmode (GPIO.BCM)
GPIO.setwarnings (False)
GPIO.setup (PEDM, GPIO.OUT)
GPIO.setup (PEDG, GPIO.OUT)
GPIO.setup (PEDR, GPIO.OUT)
GPIO.setup (CARG, GPIO.OUT)
GPIO.setup (CARY, GPIO.OUT)
GPIO.setup (CARR, GPIO.OUT)
GPIO.setup (PAINIKE, GPIO.IN)
GPIO.setup (SENSOR, GPIO.IN)
 
 
#The default state where pedestrian light is red and car light is green
GPIO.output (CARG, 1)
GPIO.output (PEDR, 1)
while True:
    #When you push the button, everything starts to happen
    b = GPIO.input (PAINIKE)
    if b == 1:
        #Pedestrian message light is turned on
        GPIO.output (PEDM, 1)
        pedPass = False
        patienceCalculator = 0
        enoughAllready = False
        print "Button has been pressed", b
        while pedPass == False:
            endtime = time.time() + 3 #Set time for how long we are looking for cars
            while time.time() < endtime:
                i = GPIO.input(SENSOR)
                if i == 1 and enoughAllready == False:
                    print "Car detected, sleep for a while", i
                    time.sleep (1) #Car detected, wait a bit
                    patienceCalculator += 1
                    if patienceCalculator > 10:
                        enoughAllready = True
                        print "Ok, too much cars!"
                   
                elif i == 0 or enoughAllready == True: # No car detected or way too bored, lets change the lights
                    print "No car detected, changing lights:"
                    GPIO.output (CARG, 0)
                    GPIO.output (CARY, 1)
                    print "car lights are yellow"
                    time.sleep (2)
                    GPIO.output (CARY, 0)
                    GPIO.output (CARR, 1)
                    time.sleep (1)
                    GPIO.output (PEDR, 0)
                    GPIO.output (PEDG, 1)
                    GPIO.output (PEDM, 0)
                    print "Car lights are red, pedestrial lights are green"
                    time.sleep (10)
                    #Pedestrian has passed so return normal state
                    print "pedestrian has crossed, changing lights"
                    GPIO.output (PEDG, 0)
                    GPIO.output (PEDR, 1)
                    time.sleep (1)
                    GPIO.output (CARR, 0)
                    GPIO.output (CARY, 1)
                   
                    print "Car lights are yellow, pedestrian lights are red"
                    time.sleep (2)
                    GPIO.output (CARY, 0)
                    GPIO.output (CARG, 1)
                    print "Car lights are green!"
                    pedPass = True
                    enoughAllready = False
                    patienceCalculator = 0
                   
                   
    elif b == 0:
        time.sleep (0.1)
 
GPIO.cleanup ()