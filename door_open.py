#This subroutine will poll pin 37 to determine the state of the door
#is it  OPEN    = True
# or    Closed  = False
#GPIO 37 = Door Close
#GPIO 16 = Return Statment


import sys
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BOARD)

DOORCLOSE = 37
DOORSTATUS = 16

# Set pin 37 to input
GPIO.setup(DOORCLOSE, GPIO.IN, pull_up_down=GPIO.PUD_UP)  

# try/finally tries to run everything in the "try" block, and ensures "finally"
# runs either way.  Used here to cleanup the GPIO pins.
try:
    if (not GPIO.input(DOORCLOSE)):
            GPIO.output(DOORSTATUS, True)           # Set pin high
            else (GPIO.output(DOORSTATUS,False))    # Set pin low
        time.sleep(0.1)
    
finally:
    GPIO.cleanup()           #Sets only pins used in this program back to input

# Clean exit
sys.exit(0)
