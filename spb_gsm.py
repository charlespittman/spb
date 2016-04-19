#!/usr/bin/env python

import serial
import RPi.GPIO as GPIO

DEBUG = True


class GSM(object):
    """Class to encapsulate the GSM module.

    Currently output-only.  Not sure how to reliably get data back from the
    module, which needs to be dealt with eventually.

    """

    def __init__(self, serial_port="/dev/ttyAMA0",
                 baudrate=9600, timeout=0.5):
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
        self._port.write("AT\r")
        print(self._port.readlines())

    def _readline(self):
        """Get line, with beginning/ending whitespace stripped."""
        return self._port.readline().strip()

    def _get_value(self, msg):
        """Returns the value of a variable in the GSM module after issuing MSG.

        The module expects a newline to terminate a command.  We just naively
        add one for now.

        """
        self._port.write(msg)
        self._port.write("\n")
        cmd = self._readline()  # Chomp cmd echo
        value = self._readline()
        empty = self._readline()  # Chomp empty line
        ok = self._readline()  # Chomp OK

        if DEBUG:
            print("cmd", cmd)
            print("empty", empty)
            print("value", value)
            print("ok", ok)

        return value

    def set_value(self, msg):
        """Sets a value in the GSM module.

        The module expects a newline to terminate a command.  We just naively
        add one for now.

        """
        self._port.write(msg)
        self._port.write("\n")
        cmd = self._readline()  # Chomp cmd echo
        reply = self._readline()  # Chomp ok

        if DEBUG:
            print("cmd", cmd)
            print("reply", reply)

        return reply

    def check_text(self):
        return self._get_value("at+cmgf?\n")

    def send_sms(self, phone_number, message):
        """Sends MESSAGE to PHONE_NUMBER using gsm module.

        PHONE_NUMBER has no special formatting (10 digits).
        """

        # This really should check that the network is connected before sending

        print("Sending SMS")

        # Sets GSM to "Text-Mode"
        self._port.write("AT+CMGF=1\n")

        # Start of an SMS cmd
        sms_cmd = 'AT+CMGS="{}"\n'.format(phone_number)
        # ASCII ctrl+z signals the end of the text
        sms_cmd += "{}\x1A".format(message)
        self._port.write(sms_cmd)


def main():
    gsm = GSM("/dev/ttyUSB0", timeout=0.5)
    gsm.begin()

    # Spam Charles with a text
    # gsm.send_sms(18433033157, "Hi")
    print(gsm.check_text())
    gsm.set_value("at+cmgf=1")

if __name__ == '__main__':
    try:
        main()
    finally:
        GPIO.cleanup()
