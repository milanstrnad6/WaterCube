#SUBMODULE:TIMES

import datetime

#ACTIONS

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
