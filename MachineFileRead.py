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

def writeCharToFile(f,ch1):
    f.write(ch1)
    #print(ch1)

def readFileFromMachine():

    try:
        f = openFileToWrite(filename)
    except:
        print("Unable to create TEMP file.")

    try:
        ser_ = openPort("COM3", 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)

        print("My" + ser_.name)
    except:
        print("Unable to open port" + ser_.name)
    ser_.timeout = 1
    ser_.xonxoff = True
    while True:
        ch = ser_.read(1)
        if ch.decode('Ascii')=="%":
            writeCharToFile(f, ch.decode('Ascii'))
            print(ch.decode('Ascii'))
            storeFile(f, ser_)
        else:
            continue


def storeFile(f,ser_):
    newFileName=""
    ch = ser_.read(1)

    writeCharToFile(f, ch.decode('Ascii'))  #write Line2 Char 1 i.e. O
    print(ch.decode('Ascii'))

    ch = ser_.read(1)   #read next char i.e. 4 from 4000

    while ch.decode('Ascii')!="\n":

        writeCharToFile(f, ch.decode('Ascii'))
        newFileName += newFileName+ch.decode('Ascii')
        print(ch.decode('Ascii'))

<<<<<<< HEAD
    print("NewFileName:" + newFileName)
    writeCharToFile(f, '\n')  # write \n to file
    print(ch.decode('Ascii'))

    while True:
        ch = ser_.read(1)
        writeCharToFile(f, ch.decode('Ascii'))  # write \n to file
        print(ch.decode('Ascii'))

        if ch.decode('Ascii')=="%":
            break
=======
        ch = ser_.read(1)
    print("NewFileName:"+newFileName)

>>>>>>> 916fe5d5a5337f0383be69cf448d261ffdffa29d
readFileFromMachine()