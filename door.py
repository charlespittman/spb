# Locks or unlocks door.

import time
import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BCM)

LOCK = 20  # Connected to Relay K2
GPIO.setup(LOCK, GPIO.OUT, initial=GPIO.HIGH)

UNLOCK = 21  # Connected to Relay K1
GPIO.setup(UNLOCK, GPIO.OUT, initial=GPIO.HIGH)


def lock_door():
    GPIO.output(LOCK, GPIO.LOW)
    time.sleep(1)
    GPIO.output(LOCK, GPIO.HIGH)
    time.sleep(1)


def unlock_door():
    GPIO.output(UNLOCK, GPIO.LOW)
    time.sleep(1)
    GPIO.output(UNLOCK, GPIO.HIGH)
    time.sleep(1)


def main():
    lock_door()
    time.sleep(1)
    unlock_door()
    time.sleep(1)
    lock_door()
    time.sleep(1)
    unlock_door()
    time.sleep(1)
    GPIO.cleanup()


if __name__ == '__main__':
    main()
