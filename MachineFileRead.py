import _thread
import time

import serial

from SerialPortFunc import detectPort, openPort, selectPort, closePort

#read char from COM while there is char available or M30 or %
#store second line of file read i.e. OXXXX
#store data in tmp file char by char
filename ="C:/Users/CC Server3/PycharmProjects/GUIPractice/CodeFiles/TEMP.txt"
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


f= openFileToWrite(filename)
detectPort()
ser_1 = openPort('COM3', 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
while ser_1.read(1):
    ch=ser_1.read(1)
    print(ch.decode('Ascii'))
    #line = ser_1.readline()
    #print("line:"+line.decode('Ascii'))
#    if line == 'M30':
 #       endofFile = 1
#    else:
 #       endofFile = 0
  #      break
    #if ch!='\n':# or ch!='%' or endofFile:
     #else:
#        ch=input("Enter char")
    writeCharToFile(ch.decode('Ascii'))


    #if ser_1.timeout(1):
     #   break
# Define a function for the thread
"""
def createFile( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
f.close()
# Create two threads as follows
try:
   _thread.start_new_thread( createFile, ("Thread-1", 2, ) )
   _thread.start_new_thread( createFile, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")
"""