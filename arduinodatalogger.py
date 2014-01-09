# ARDUINO DATA LOGGER
# (C) 2013 Geoffrey "GEOFBOT" Mon

import serial
from sys import argv, exit

if len(argv) != 2:
    exit("Command argument needed for target filename.")

device = serial.Serial("COM3", 9600, xonxoff = True)

print("Press Ctrl-C to quit.")

run = True

while run:
    try:
        if device.readable():
            line = device.readline().decode().rstrip('\n')
            with open(argv[1], 'a') as log:
                log.write(line)
            print(line)
    except KeyboardInterrupt:  
        run = False  
