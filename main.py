#!/usr/bin/env python

import Adafruit_PN532 as PN532
import RPi.GPIO as GPIO
import binascii
import spb_cam
import spb_door
import spb_gsm
import time

DEBUG = True
PHONE = 14047961224
RFID_CARD = '0d345b95'

# Set up the objects we'll be using later.
door = spb_door.Door(lock_pin=20, unlock_pin=21, switch_pin=5, mail_pin=16)
door.lock()

gsm = spb_gsm.GSM("/dev/ttyAMA0", timeout=0.5)
gsm.begin()

rfid = PN532.PN532(cs=18, sclk=25, mosi=23, miso=24)
rfid.begin()
rfid.SAM_configuration()


def mail_switch_cb(mail_switch):
    """Sends alert when mail is detected."""
    if DEBUG:
        print("ALERT: Mail")
    else:
        send_msg(PHONE, "You have mail")


def door_switch_cb(door_switch):
    """Sends alert and take pictures if the door is broken into."""
    if door.is_open():
        if door.locked:
            if DEBUG:
                print("ALERT: Door opened while locked.")
            else:
                spb_cam.take_sequence()
                send_msg(PHONE, "Unauthorized entry.")

        if door.unlocked:
            if DEBUG:
                print("INFO: Door opened while unlocked.")

    if door.is_closed():
        if DEBUG:
            print("INFO: Door closed. Locking up.")
        time.sleep(0.5)  # Give the door a chance to finish closing
        door.lock()


def lock_switch_cb(lock_switch):
    """Toggles the lock."""
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

    # Button to lock/unlock
    GPIO.add_event_detect(lock_switch, GPIO.FALLING,
                          callback=lock_switch_cb, bouncetime=1000)

    # Detect mail
    GPIO.add_event_detect(door.mail_pin, GPIO.FALLING,
                          callback=mail_switch_cb, bouncetime=1000)

    # Detect door open/close
    GPIO.add_event_detect(door.switch_pin, GPIO.BOTH,
                          callback=door_switch_cb, bouncetime=1000)

    if DEBUG:
        print("INFO: Waiting for RFID card.")
    while True:
            uid = rfid.read_passive_target()

            if uid is None:
                continue

            if binascii.hexlify(uid) == RFID_CARD:
                if DEBUG:
                    print("INFO: Found correct RFID card.")
                door.unlock()
            else:
                if DEBUG:
                    print("INFO: Found wrong RFID card.")

            time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
