import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#Initializing variables
moveSpeed=50
timeDelay=3
turnSpeed=80
turnDelay=5
obsDistance=45
#Setup pins for Motors
PINFL = 10
PINFR = 18
PINBL = 12
PINBR = 16
GPIO.setup(PINFL,GPIO.OUT)
GPIO.setup(PINFR,GPIO.OUT)
GPIO.setup(PINBL,GPIO.OUT)
GPIO.setup(PINBR,GPIO.OUT)
fl=GPIO.PWM(PINFL,207)
fr=GPIO.PWM(PINFR,207)
bl=GPIO.PWM(PINBL,207)
br=GPIO.PWM(PINBR,207)
fl.start(0)
fr.start(0)
bl.start(0)
br.start(0)
#Setup pins for Ultrasonic Sensor
TRIG = 24
ECHO = 22
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
#Functions
def move(pin,spd):
    print "moving..."
    pin.ChangeDutyCycle(spd)
def stop(pin):
    print "stoping..."
    pin.ChangeDutyCycle(0)
def stopAll():
    print "stoping..."
    fl.ChangeDutyCycle(0)
    fr.ChangeDutyCycle(0)
    bl.ChangeDutyCycle(0)
    br.ChangeDutyCycle(0)
    time.sleep(moveDelay)
def forward(pin):
    print "moving forwards"
    move(pin,moveSpeed)
def forwardAll():
    print "moving all wheels"
    move(fl,moveSpeed)
    move(fr,moveSpeed)
    move(bl,moveSpeed)
    move(br,moveSpeed)
    time.sleep(moveDelay)
def turn(pin1,pin2):
    print "turning..."
    move(pin1,turnSpeed)
    move(pin2,turnSpeed)
    time.sleep(turnDelay)
def turnLeft():
    print "turning left"
    turn(tr,br)
    time.sleep(turnDelay)
def turnRight():
    print "turning right"
    turn(tl,bl)
    time.sleep(turnDelay)
def getDistance():
    GPIO.output(TRIG,False)
    print "Waiting for sensor to settle"
    time.sleep(1)
    
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulseStart = time.time()
    while GPIO.input(ECHO)==1:
        pulseEnd = time.time()
    pulseDuration=pulseEnd-pulseStart
    distance=pulseDuration * 17150
    distance=round(distance,2)
    print "Distance:",distance,"cm"
    return distance
#Main method
    #test methods
while True:
    forwardAll()
    if(getDistance()<obsDistance):
        turnLeft()
        forwardAll()
        turnRight()
#End main method
fl.stop()
fr.stop()
bl.stop()
br.stop()
GPIO.cleanup()