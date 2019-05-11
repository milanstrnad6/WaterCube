#MODULE:ULTRASOUND(short:US)

import RPi.GPIO as IO
import time

US_OUT = 18
US_IN = 24

#SETUP

def setup():
    print("ULTRASOUND - SETUP")
    IO.setmode(IO.BCM)
    IO.setup(US_OUT, IO.OUT)
    IO.setup(US_IN, IO.IN)

#ACTIONS

def getDistance():
    print("ULTRASOUND - GET DISTANCE...")

    #For sure.
    time.sleep(0.01)

    #Sending sound for duration 0.00001 seconds.
    IO.output(US_OUT, 1)
    time.sleep(0.00001)
    IO.output(US_OUT, 0)

    #Prepare properties for measuring time.
    timeStart = time.time()
    timeStop = time.time()

    #Listen for sound coming back.
    while IO.input(US_IN) == 0:
 	timeStart = time.time()
    while IO.input(US_IN) == 1:
	timeStop = time.time()

    #Calculate distance.
    timeElapsed = timeStop - timeStart
    distance = (timeElapsed * 34300) / 2

    print("ULTRASOUND - GET DISTANCE... [%.1f CM]" % distance)
    return distance

#TEST

def test():
    print("ULTRASOUND - TEST")
    IO.setwarnings(0)
    setup()
    getDistance()

#test()
