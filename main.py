#!/usr/bin/env python

import Adafruit_PN532 as PN532
import RPi.GPIO as GPIO
import spb_door
import spb_gsm
import serial
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


def alert_mail(door.mail_pin):
    """Sends text to say mail has arrived."""
    if DEBUG:
        print("ALERT: Mail")
    else:
        send_msg(PHONE, "You have mail")


def mail_switch():
    """Use mail_switch.py to check for mail, If present if will call send_mail.py."""
    pass


def send_msg(phone_number, message):
    """Sends MESSAGE to PHONE_NUMBER."""
    gsm.send_sms(phone_number, message)


def cam():
    """Takes a picture from cam.py and stores in on the card and calls send_alert.py"""
    pass


def intrusion_check():
    """Monitors the status of door while locked and calls cam() if opened"""
    pass


def main():
    GPIO.add_event_detect(door.mail_pin, GPIO.FALLING,
                          callback=alert_mail, bouncetime=1000)

    while True:
        print("Loop")
        time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
