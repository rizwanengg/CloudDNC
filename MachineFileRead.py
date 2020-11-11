import _thread
import time

import os
import serial

from ReadJSON import getTempFileURL, getFolderURL
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

def readFileFromMachine(ser):

    try:
        f = openFileToWrite(filename)
    except:
        print("Unable to create TEMP file.")

    try:
   #     ser_ = openPort("COM3", 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
        ser_ = ser

        print("My" + ser_.name)
    except:
        print("Unable to open port" + ser_.name)

  #  ser_.timeout = 1
  #  ser_.xonxoff = True

    while True:
        ch = ser_.read(1)
        if ch.decode('Ascii')=="%":
            writeCharToFile(f, ch.decode('Ascii'))  #write % char in file
            print(ch.decode('Ascii'))
            newFile=storeFile(f, ser_)
            f.close()
            try:
                os.rename(getTempFileURL(),getFolderURL()+newFile)
            except IOError:
                print("Unable to save incoming file from Machine. May be the file is already available.")
        else:
            continue


def storeFile(f,ser_):
    newFileName=""
    ch = ser_.read(1)
    ch = ser_.read(1)
    #writeCharToFile(f, ch.decode('Ascii'))  #write Line1 end char i.e. \n
  #  print(ch.decode('Ascii'))

    ch = ser_.read(1)

    writeCharToFile(f, ch.decode('Ascii'))  # write Line2 first char i.e. O or P or...
    print(ch.decode('Ascii'))

    ch = ser_.read(1)   #read next char i.e. 4 from 4000

    while ch.decode('Ascii')!='\r':

        writeCharToFile(f, ch.decode('Ascii'))
        newFileName += ch.decode('Ascii')
        print(ch.decode('Ascii'))
        ch = ser_.read(1)  # read next char

    print("NewFileName:" + newFileName)
    writeCharToFile(f, '\n')  #write Line2 end char i.e. \n
    print(ch.decode('Ascii'))

    while True:
        ch = ser_.read(1)
        writeCharToFile(f, ch.decode('Ascii'))  # write \n to file
        print(ch.decode('Ascii'))

        if ch.decode('Ascii')=="%" or ch.decode('Ascii')==32:
            break

    return newFileName
#readFileFromMachine()