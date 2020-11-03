import serial
import glob
import sys
import io

def detectPort():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
#def sendChar(ch):
def selectPort():
    comlist = detectPort()
    print(comlist)
    print("Port Selected is:"+ comlist[0])
    return comlist[0]

def openPort(portno_,brate_,data_bits,parity_,stop_bits):
    #port=None, baudrate=9600, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=None,
    # xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None, exclusive=None)
    ser = serial.Serial(portno_,brate_,data_bits,parity_,stop_bits,timeout=1)   # open serial port
    """ser.baudrate = brate
    ser.stopbits = sbits
    ser.parity = pari
    ser.port = selectPort()
    ser.bytesize = databits
    ser.timeout = None

    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
    sio.write(serial.unicode("hello\n"))
    sio.flush()  # it is buffering. required to get the data out *now*
    hello = sio.readline()"""
  #  print(serial.unicode("hello\n"))
    print("Port " + ser.name + " Opened")

    return ser#,sio

def closePort(ser1):
   try:
    ser1.close()
    print("Port "+ser1.name+" Closed")
   except serial.SerialException:
    print(serial.SerialException)

detectPort()
#selectPort()
ser_ = openPort(selectPort(),9600,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE)
#par = "{}".format("None")
#par ="{!r}".format("N")
#print (par)
#ser_ = openPort(selectPort(),9600,8,par,serial.STOPBITS_ONE)
ch1='Hello\n'
ser_.write(ch1.encode())  # write a string
ser_.close()

#closePort(ser_)