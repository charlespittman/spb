#!/usr/bin/env python

import Adafruit_PN532 as PN532
import RPi.GPIO as GPIO
import spb_cam
import spb_door
import spb_gsm
import time

DEBUG = True

# Set up the objects we'll be using later.
door = spb_door.Door(lock_pin=20, unlock_pin=21, switch_pin=12, mail_pin=16)
door.lock()

gsm = spb_gsm.GSM("/dev/ttyAMA0", timeout=0.5)
gsm.begin()

rfid = PN532.PN532(cs=18, sclk=25, mosi=23, miso=24)
rfid.begin()
rfid.SAM_configuration()

PHONE = 14047961224


def mail_switch_cb(mail_switch):
    """Callback function when the mail switch triggers."""
    if DEBUG:
        print("ALERT: Mail")
    else:
        send_msg(PHONE, "You have mail")


def door_switch_cb(door_switch):
    if DEBUG:
        if door.locked:
    """Callback function when the door is opened."""
            print("ALERT: Door opened while locked.")
        if door.unlocked:
            print("INFO: Door opened while unlocked.")


def lock_switch_cb(lock_switch):
    """Callback function when the lock button is pressed."""
    if door.locked:
        door.unlock()
    else:
        door.lock()


def send_msg(phone_number, message):
    """Sends MESSAGE to PHONE_NUMBER."""
    gsm.send_sms(phone_number, message)


def main():
    lock_switch = 17
    GPIO.setup(lock_switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(lock_switch, GPIO.FALLING,
                          callback=lock_switch_cb, bouncetime=1000)

    GPIO.add_event_detect(door.mail_pin, GPIO.FALLING,
                          callback=mail_switch_cb, bouncetime=1000)

    GPIO.add_event_detect(door.switch_pin, GPIO.FALLING,
                          callback=door_switch_cb, bouncetime=1000)

    while True:
        print("Loop")
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
