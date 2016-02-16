from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

IR_PIN = 4
GPIO.setup(IR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# try/finally tries to run everything in the "try" block, and ensures "finally"
# runs either way.  Used here to cleanup the GPIO pins.
try:
    while True:
        if GPIO.input(IR_PIN):
            # beam closed
            print('1')
        else:
            # beam broken
            print('0')
        sleep(0.1)
finally:
    GPIO.cleanup()
