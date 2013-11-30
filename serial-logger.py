# Serial data logger
# Based on http://forum.keithley.com/phpBB3/viewtopic.php?f=32&t=13020

"""
Connects to a serial device and continously requests and prints data.
"""

import serial
import time

device = serial.Serial("COM1", 9600, xonxoff = True)

while True:
    device.write(":FETCh?\r\n")
    time.sleep(0.1)
    out = ""
    while device.inWaiting() > 0:
        out += device.read(1)
    if out != '':
        out = out.rstrip()
        print(time.time() + "," + out)
