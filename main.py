#!/usr/bin/env python

import Adafruit_PN532 as PN532
import RPi.GPIO as GPIO
import door.Door as Door
import gsm.GSM as GSM
import serial


# Set up the objects we'll be using later.
door = Door(lock_pin=20, unlock_pin=21, switch_pin=12)
door.lock()

gsm = GSM("/dev/ttyUSB0", timeout=0.5)
gsm.begin()

rfid = PN532.PN532(cs=18, sclk=25, mosi=23, miso=24)
rfid.begin()
rfid.SAM_configuration()


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
    pass


if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
