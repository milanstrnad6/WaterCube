#MODULE:HISTORY

import files as FILES
import times as TIMES

#PROPERTIES

FILENAME = 'history.txt'

#ACTIONS: LOAD

def loadAllEvents():
    print("HISTORY - LOAD ALL EVENTS")
    return FILES.load(FILENAME)

#ACTIONS: SAVE

def saveEventDeviceInit():
    print("HISTORY - SAVE EVENT: DEVICE INIT")
    saveEvent("deviceInit")

def saveEventManualPour(seconds):
    print("HISTORY - SAVE EVENT: MANUAL POUR")
    saveEvent("manualPour",seconds)

def saveEventAutomaticPour(seconds):
    print("HISTORY - SAVE EVENT: AUTOMATIC POUR")
    saveEvent("automaticPour",seconds)

def saveEventWarning():
    print("HISTORY - SAVE EVENT: WARNING")
    saveEvent("warning")

#UTILITIES

def saveEvent(type,seconds=0):
    print("HISTORY - SAVE EVENT")
    data = FILES.load(FILENAME)
    record = type + "|" + TIMES.now() + "|" + str(seconds) + "\n"
    data.append(record)
    FILES.save(FILENAME,data)

def reset():
    data = 'HISTORY\n'
    FILES.save(FILENAME,data)

def test():
    type = "manualPouring"
    time = TIMES.now()
    saveEvent(type,time)
