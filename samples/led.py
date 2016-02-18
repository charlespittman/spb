import sys
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)

LED = 11
GPIO.setup(LED, GPIO.OUT)  # Set pin 11 to output

# try/finally tries to run everything in the "try" block, and ensures "finally"
# runs either way.  Used here to cleanup the GPIO pins.
try:
    GPIO.output(LED, True)  # Set pin high
    GPIO.output(LED, False)  # Set pin low
finally:
    GPIO.cleanup()

# Clean exit
sys.exit(0)
