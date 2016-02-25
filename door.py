# Locks or unlocks door.

import time
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)

LOCK = 20  # Connected to Relay K2
GPIO.setup(LOCK, GPIO.OUT, initial=GPIO.HIGH)

UNLOCK = 21  # Connected to Relay K1
GPIO.setup(UNLOCK, GPIO.OUT, initial=GPIO.HIGH)

door_switch = 12
GPIO.setup(door_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def lock_door():
    """Locks door on Relay K2"""
    GPIO.output(LOCK, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LOCK, GPIO.HIGH)


def unlock_door():
    """Unlocks door on Relay K1."""
    GPIO.output(UNLOCK, GPIO.LOW)
    time.sleep(1)
    GPIO.output(UNLOCK, GPIO.HIGH)


def is_closed():
    """Return True if door is closed."""
    if GPIO.input(door_switch):
        return True
    else:
        return False


def is_open():
    """Return True if door is open."""
    if is_closed():
        return False
    else:
        return True


def main():
    print("Lock")
    lock_door()
    time.sleep(2)
    print("Unlock")
    unlock_door()
    time.sleep(2)
    print("Lock")
    lock_door()
    time.sleep(2)
    print("Unlock")
    unlock_door()
    time.sleep(2)


if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
