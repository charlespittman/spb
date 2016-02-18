# This subroutine will poll pin 37 to determine the state of the door.

import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)

DOORCLOSE = 37
DOORSTATUS = 16

GPIO.setup(DOORCLOSE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    if (not GPIO.input(DOORCLOSE)):
        GPIO.output(DOORSTATUS, True)
    else:
        GPIO.output(DOORSTATUS, False)

finally:
    GPIO.cleanup()  # Sets only pins used in this program back to input
