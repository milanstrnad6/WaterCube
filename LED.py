#MODULE:LED

import RPi.GPIO as IO
import time

LED_BLUE = 20
LED_RED = 16

#SETUP

def setup():
    print("LED - SETUP")
    IO.setmode(IO.BCM)
    IO.setup(LED_BLUE, IO.OUT)
    IO.setup(LED_RED, IO.OUT)

#ACTIONS

def bootBlinking(duration):
    print("LED - BOOT BLINKING...")
    ledOff()
    for x in range (0, (duration - 1)):
	time.sleep(0.5)
	ledRed()
	time.sleep(0.5)
	ledOff()
    time.sleep(1)
    ledBlue()

#UTILITIES

def ledBlue():
    print("LED - BLUE")
    IO.output(LED_BLUE, 1)

def ledRed():
    print("LED - RED")
    IO.output(LED_RED, 1)

def ledOff():
    print("LED - OFF")
    IO.output(LED_BLUE, 0)
    IO.output(LED_RED, 0)

#TEST

def test():
    print("LED - TEST")
    IO.setwarnings(0)
    setup()
    #bootBlinking()
    ledOff()

#test()
