#BOOT MODULE:CUBE

import RPi.GPIO as IO

import SCHEDULE
import ULTRASOUND
import PUMP
import LED

#BOOT

def boot(duration):
    print("*[CUBE - BOOT]*")

    IO.setmode(IO.BCM)
    IO.setwarnings(0)

    ULTRASOUND.setup()
    PUMP.setup()
    LED.setup()

    LED.bootBlinking(duration)
    start()

#LOGIC

def start():
    print("*[CUBE - START]*")

    #if SCHEDULE.shouldPour():
    	#print("*CUBE - SHOULD POUR = YES")


