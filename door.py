# Locks or unlocks door.

import RPi.GPIO as GPIO

# Set pin numbering to Broadcom type
GPIO.setmode(GPIO.BOARD)

LOCK = 7  # Connected to Relay K2
GPIO.setup(LOCK, GPIO.OUT)

UNLOCK = 8  # Connected to Relay K1
GPIO.setup(UNLOCK, GPIO.OUT)


def lock_door():
    GPIO.output(LOCK, False)


def unlock_door():
    GPIO.output(UNLOCK, False)
