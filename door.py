# Locks or unlocks door.

import time
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)


class Door(object):
    """Class to encapsulate the GSM module."""

    def __init__(self, lock_pin, unlock_pin, switch_pin):
        """Set up the Door instance.

        Args:
        lock_pin = Attached to the locking relay
        unlock_pin = Attached to the unlocking relay
        switch_pin = Attached to the sensor detecting open/close
        """

        self.lock_pin = lock_pin
        GPIO.setup(self.lock_pin, GPIO.OUT, initial=GPIO.HIGH)

        self.unlock_pin = unlock_pin
        GPIO.setup(self.unlock_pin, GPIO.OUT, initial=GPIO.HIGH)

        self.switch_pin = switch_pin
        GPIO.setup(self.switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def lock(self):
        """Locks door on Relay K2 only if door is closed."""

        # Fail unless the door is closed.
        assert self.is_closed(), "Won't lock door while it's open."

        GPIO.output(self.lock_pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.lock_pin, GPIO.HIGH)

    def unlock(self):
        """Unlocks door on Relay K1 if door is closed."""

        # Fail unless the door is closed.
        assert self.is_closed(), "Won't unlock door while it's open."

        GPIO.output(self.unlock_pin, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.unlock_pin, GPIO.HIGH)

    def is_closed(self):
        """Return True if door is closed."""
        return GPIO.input(self.switch_pin) == GPIO.LOW

    def is_open(self):
        """Return True if door is open."""
        return GPIO.input(self.switch_pin) == GPIO.HIGH


def main():
    door = Door(20, 21, 12)

    print("Lock")
    door.lock()
    time.sleep(2)
    print("Unlock")
    door.unlock()
    time.sleep(2)
    print("Lock")
    door.lock()
    time.sleep(2)
    print("Unlock")
    door.unlock()
    time.sleep(2)


if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
