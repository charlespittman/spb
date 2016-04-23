#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

DEBUG = False

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)


class Door(object):
    """Class to encapsulate the door module."""

    def __init__(self, lock_pin, unlock_pin, switch_pin, mail_pin):
        self.locked = False
        self.unlocked = True

        self.lock_pin = lock_pin
        GPIO.setup(self.lock_pin, GPIO.OUT, initial=GPIO.HIGH)

        self.unlock_pin = unlock_pin
        GPIO.setup(self.unlock_pin, GPIO.OUT, initial=GPIO.HIGH)

        self.switch_pin = switch_pin
        GPIO.setup(self.switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.mail_pin = mail_pin
        GPIO.setup(self.mail_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def lock(self):
        """Locks door on Relay K2"""
        if DEBUG:
            print("INFO: Locking door.")
        GPIO.output(self.lock_pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.lock_pin, GPIO.HIGH)
        self.locked = True
        self.unlocked = False

    def unlock(self):
        """Unlocks door on Relay K1."""
        if DEBUG:
            print("INFO: Unlocking door.")
        GPIO.output(self.unlock_pin, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.unlock_pin, GPIO.HIGH)
        self.locked = False
        self.unlocked = True

    def is_closed(self):
        """Return True if door is closed."""
        return GPIO.input(self.switch_pin) == GPIO.LOW

    def is_open(self):
        """Return True if door is open."""
        return GPIO.input(self.switch_pin) == GPIO.HIGH


def main():
    door = Door(lock_pin=20, unlock_pin=21, switch_pin=12, mail_pin=16)

    print("Lock")
    door.lock()
    print('Door is {}.'.format('Locked' if door.locked else 'Unlocked'))
    time.sleep(2)

    print("Unlock")
    door.unlock()
    print('Door is {}.'.format('Locked' if door.locked else 'Unlocked'))
    time.sleep(2)

    print("Lock")
    door.lock()
    print('Door is {}.'.format('Locked' if door.locked else 'Unlocked'))
    time.sleep(2)

    print("Unlock")
    door.unlock()
    print('Door is {}.'.format('Locked' if door.locked else 'Unlocked'))
    time.sleep(2)


if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
