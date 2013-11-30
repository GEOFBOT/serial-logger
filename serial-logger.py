# KEITHLEY DATA LOGGER
# (C) 2013 Geoffrey "GEOFBOT" Mon

"""
Connects to a serial device and continously requests and logs data.
"""

# Import our modules.
import serial
import msvcrt

device = serial.Serial("COM3", 9600, xonxoff = True)
log = open("serial-logger.log", 'w')

print("Press Ctrl-C to quit.")

run = True

while run:
    try:
        device.write("data?")
        if device.readable():
            log.write(device.readline() + '\n')
    except KeyboardInterrupt:  
        run = False
    
log.close()    




