import _thread
import time

import serial

from ReadJSON import getTempFileURL
from SerialPortFunc import detectPort, openPort, selectPort, closePort

#read char from COM while there is char available or M30 or %
#store second line of file read i.e. OXXXX
#store data in tmp file char by char
filename =getTempFileURL()
global f

def openFileToWrite(filename):
    try:
        f = open(filename, "w")
        return f
    except IOError:
        print("File Opening Error!")

def writeCharToFile(ch1):
    f.write(ch1)
    print(ch1)

def readFileFromMachine():

    try:
        f = openFileToWrite(filename)
    except:
        print("Unable to create TEMP file.")
    # detectPort()

    try:
        ser_ = openPort("COM3", 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
        ser_.timeout = 1
        print("My" + ser_.name)
    except:
       # print(serial.SerialException)
        print("Unable to open port" + ser_.name)
    while ser_.read(1):
     #
            writeCharToFile("%")
            storeFile(ser_)
      #  else:
       #     continue

def storeFile(ser_):
    while ser_.read(1):
        ch = ser_.read(1)
        print(ch.decode('Ascii'))
        writeCharToFile(ch.decode('Ascii'))

readFileFromMachine()