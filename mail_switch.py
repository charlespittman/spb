#This subroutine will poll pin 36 to determine if is was pressed
#GPIO 36 = mail trigger
#GPIO 32 = yes mail


import sys
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BOARD)

MAILSWITCH = 36
YESMAIL = 32

# Set pin 36 to input
GPIO.setup(MAILSWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# try/finally tries to run everything in the "try" block, and ensures "finally"
# runs either way.  Used here to cleanup the GPIO pins.

try:
    while(True):
        if (not GPIO.input(MAILSWITCH)):
            GPIO.output(YESMAIL, True)  # Set pin high
        time.sleep(0.1)
    
finally:
    GPIO.cleanup()           #Sets only pins used in this program back to input

# Clean exit
sys.exit(0)
