# This subroutine will poll pin 36 to determine if is was pressed

import time
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)

mail_switch = 16
GPIO.setup(mail_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

LED = 26
GPIO.setup(LED, GPIO.OUT, initial=GPIO.HIGH)


def is_mail():
    """Return True if mail_switch is triggered."""
    return GPIO.input(mail_switch) == GPIO.LOW


def send_mail():
    """Send mail message."""
    # Just using an LED for now.
    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LED, GPIO.HIGH)


def main():
    """Poll for mail trigger."""
    try:
        while(True):
            GPIO.wait_for_edge(mail_switch, GPIO.FALLING)
            send_mail()

    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
