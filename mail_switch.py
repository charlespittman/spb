# This subroutine will poll pin 36 to determine if is was pressed

import time
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)

MAILSWITCH = 16
GPIO.setup(MAILSWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LED = 26
GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)


def is_mail():
    """Return True if MAILSWITCH is triggered."""
    if not GPIO.input(MAILSWITCH):
        return True
    else:
        return False


def send_mail():
    """Send mail message."""
    # Just using an LED for now.
    GPIO.output(LED, GPIO.LOW)


def main():
    """Poll for mail trigger."""
    try:
        while(True):
            if is_mail():
                send_mail()
            else:
                GPIO.output(LED, GPIO.HIGH)
            time.sleep(0.1)

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
