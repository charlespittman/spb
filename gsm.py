#!/usr/bin/env python

import serial
from time import sleep


class GSM(object):
    """Class to encapsulate the GSM module."""

    def __init__(self, serial_port="/dev/ttyAMA0",
                 baudrate=115200, timeout=30):
        """Set up serial connection to GSM module."""

        self._serial_port = serial_port
        self._baudrate = baudrate
        self._timeout = timeout

        self._port = serial.Serial(self._serial_port, self._baudrate,
                                   timeout=self._timeout)

    def begin(self):
        """Initialize communication with the GSM module.  Must be called before any
other calls are made.

        """
        print("Initialising Modem...")

        # The module sets the baudrate automatically based on the first
        # message.
        self._port.write("AT\n")
        self._readline()
        self._readline()

    def _readline(self):
        self._port.readline().strip()

    def send_sms(self, phone_number, message):
        """Sends MESSAGE to PHONE_NUMBER using gsm module at PORT

PHONE_NUMBER has no special formatting (10 digits).
        """

        # This really should check that the network is connected before sending

        print("Sending SMS")

        # Sets GSM to "Text-Mode"
        self._port.write("AT+CMGF=1\n")
        self._readline()
        self._readline()

        # Start of an SMS cmd
        sms_cmd = 'AT+CMGS="{}"\n'.format(phone_number)
        # ASCII ctrl+z signals the end of the text
        sms_cmd += "{}\x1A".format(message)
        self._port.write(sms_cmd)

        sleep(30)    # Sometimes takes a while to send
        self._readline()
        self._readline()
        self._readline()
        self._readline()
        self._readline()


def main():
    gsm = GSM("/dev/ttyUSB0")
    gsm.begin()

    # Spam Charles with a text
    gsm.send_sms(18433033157, "Hi")

if __name__ == '__main__':
    main()
