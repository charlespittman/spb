#This subroutine will set pin 8 to high turning on Relay K1
#GPIO 8 = Open


import sys
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BOARD)

UNLOCK = 8
GPIO.setup(UNLOCK, GPIO.OUT)  # Set pin 7 to output

# try/finally tries to run everything in the "try" block, and ensures "finally"
# runs either way.  Used here to cleanup the GPIO pins.
try:
    GPIO.output(UNLOCK, True)  # Set pin high
    
finally:
    GPIO.cleanup()          #Sets only pins used in this program to input

# Clean exit
sys.exit(0)
