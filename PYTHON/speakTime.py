#! /usr/bin/python3
# speakTime <minute-interval>
# Speaks time in hours & minutes with AM / PM.

import pyttsx3
from datetime import datetime
import time

import sys

def already_running(script_basename):
    import psutil

    check_name = script_basename.lower()

    for proc in psutil.process_iter():
        print(proc)
        try:
            if (check_name in proc.name().lower()) and (str(proc.status()).lower() != 'zombie'):
                if (os.getpid() != proc.pid):
                    return True
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return False

###################################################


interval=int(sys.argv[1])

if len(sys.argv) > 2:
    volume=float(sys.argv[2])
else:
    volume = 0.9

engine = pyttsx3.init()
engine.setProperty('volume', volume)

import os
this_file = os.path.basename(__file__)

if already_running(this_file):
    ALREADY_MSG = "Exiting: " + this_file + " is already running."
    print(ALREADY_MSG)
    engine.say(ALREADY_MSG)
    engine.runAndWait()

    sys.exit(1)


while True:
    now = datetime.now()

    tnow = "12" if ((now.hour % 12) == 0) else str(now.hour % 12)

    if (now.minute != 0):
        if (now.minute < 10):
            tnow += "," + "O" + str(now.minute)
        else:
            tnow += "," + str(now.minute)

    tnow += ",A.M." if (now.hour < 12) else ",P.M."

    engine.say("Hello! The time is now " + tnow)
    engine.runAndWait()

    remsecs= ((interval - (now.minute % interval) ) * 60) - now.second

    print(tnow)
    print(remsecs)

    time.sleep(remsecs)
done
