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

        print("Initialising Modem...")

        self.serialport = serial.Serial(self._port, self._baudrate,
                                        timeout=self._timeout)

        # The module sets the baudrate automatically based on the first
        # message.
        self.serialport.write("AT\n")
        print(self.serialport.readline().strip())
        print(self.serialport.readline().strip())

    def _readline(self):
        self._port.readline().strip()

    def send_sms(self, phone_number, message):
        """Sends MESSAGE to PHONE_NUMBER using gsm module at PORT

PHONE_NUMBER has no special formatting (10 digits).
        """

        # This really should check that the network is connected before sending

        print("Sending SMS")

        # Sets GSM to "Text-Mode"
        self.serialport.write("AT+CMGF=1\n")
        print(self.serialport.readline().strip())
        print(self.serialport.readline().strip())

        # Start of an SMS cmd
        sms_cmd = 'AT+CMGS="{}"\n'.format(phone_number)
        # ASCII ctrl+z signals the end of the text
        sms_cmd += "{}\x1A".format(message)
        self.serialport.write(sms_cmd)

        sleep(30)    # Sometimes takes a while to send
        print(self.serialport.readline().strip())
        print(self.serialport.readline().strip())
        print(self.serialport.readline().strip())
        print(self.serialport.readline().strip())
        print(self.serialport.readline().strip())


def main():
    g = GSM()

    # Spam Charles with a text
    g.send_sms(18433033157, "Hi")

if __name__ == '__main__':
    main()
