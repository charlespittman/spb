# This subroutine will poll pin 36 to determine if is was pressed

import time
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)

MAILSWITCH = 36
YESMAIL = 32

GPIO.setup(MAILSWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def is_mail():
    """Return True if MAILSWITCH is triggered."""
    if not GPIO.input(MAILSWITCH):
        return True
    else:
        return False


def send_mail():
    """Send mail message."""
    pass


def main():
    """Poll for mail trigger."""
    try:
        while(True):
            if is_mail():
                send_mail()
                time.sleep(0.1)

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
