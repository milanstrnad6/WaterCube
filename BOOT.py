#BOOT

import CUBE
import subprocess

#PROPERTIES

WAIT_FOR_INTERNET_CONNECTION = 10

#BOOTING

print("BOOTING...")

CUBE.boot(WAIT_FOR_INTERNET_CONNECTION)
subprocess.call(['/home/pi/CUBE/serverStart.sh'])

#Nothing more can be done here.
#------------------------------
