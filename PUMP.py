#MODULE:PUMP

import RPi.GPIO as IO
import time

PUMP = 12

ON = 0
OFF = 1

#SETUP

def setup():
    print("PUMP - SETUP")
    IO.setmode(IO.BCM)
    IO.setup(PUMP, IO.OUT)
    IO.output(PUMP, OFF)

#ACTIONS

def start(duration):
    print("PUMP - START [DURATION = %.1f]" % duration)
    IO.output(PUMP, ON)
    time.sleep(duration)
    IO.output(PUMP, OFF)

def stop():
    print("PUMP - STOP")
    IO.output(PUMP, 1)

#TEST

def test():
    print("PUMP - TEST")
    IO.setwarnings(0)
    setup()
    #start(2)
    stop()

#test()
