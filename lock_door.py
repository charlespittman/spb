#This subroutine will set pin 7 to high turning on Relay K2
#GPIO 7 = Close


import sys
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BOARD)

LOCK = 7
GPIO.setup(LOCK, GPIO.OUT)  # Set pin 7 to output

# try/finally tries to run everything in the "try" block, and ensures "finally"
# runs either way.  Used here to cleanup the GPIO pins.
try:
    GPIO.output(LOCK, True)  # Set pin high
    
finally:
    GPIO.cleanup()           #Sets only pins used in this program back to input

# Clean exit
sys.exit(0)
