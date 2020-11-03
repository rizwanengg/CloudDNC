import _thread
import sys

import easygui
import serial
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

#from MachineFileRead import readFileFromMachine
from ReadJSON import *
from SerialPortFunc import detectPort, openPort, selectPort
try:
    ser = openPort(selectPort(), 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
 #   _thread.start_new_thread(readFileFromMachine(), ser, ("RF"))

except:
    print(IOError)


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.initUI()
        self.sendBtn.clicked.connect(self.on_sendBtn1_clicked)
        self.pauseBtn.clicked.connect(self.on_pauseBtn1_clicked)
        self.resumeBtn.clicked.connect(self.on_resumeBtn1_clicked)
        self.abortBtn.clicked.connect(self.on_abortBtn1_clicked)
        self.restartBtn.clicked.connect(self.on_restartBtn1_clicked)
        self.backBtn.clicked.connect(self.on_backBtn1_clicked)
        list_of_ports = detectPort()
        print(list_of_ports)
    def initUI(self):
        loadUi('MainScreen.ui', self)

    def on_sendBtn1_clicked(self):
        print("Send Btn Clicked")
        file_path_string = ""
        try:
            self.displayFile()
        except(IOError,Exception):
            print(Exception)

    def displayFile(self):
        file_path_string = easygui.fileopenbox(msg="Select single file at a time.", title="Choose",
                                               default=getFolderURL(),
                                               filetypes=None, multiple=False)
        file_path_string = (file_path_string.replace('\\', "/"))
        x = file_path_string.split("/")
        l = len(x)

        file_path = getFolderURL()+x[l - 1]
        print(file_path)
        #print(getPortNo(), getBrate(), getDataBits(), getParity(), getStopBits())
     #   detectPort()

        fileptr = open(file_path, "r")
        self.sendFile1(ser,fileptr)
        try:
            _thread.start_new_thread(self.sendFile1,ser,fileptr, (x))

        except:
            print("File Sent.")

    def sendFile1(self,ser,fileptr1):
        lineno = 0;
        while True:
            line = fileptr1.readline()
        #    QMessageBox.information(self, "Info", line)
            lineno += 1
            if not line:
                break
            self.split_to_char(ser,line)

            full_line = "{}".format(lineno) + "  " + line.strip()
            self.addLineToFileDisplay(full_line)
        fileptr1.close()


    def split_to_char (self,ser,word):
        for x in range(len(word)):
            ch1=word[x]
            ser.write(ch1.encode())
            print(ch1)


    def on_pauseBtn1_clicked(self):
        print("Pause Btn Clicked")

    def on_resumeBtn1_clicked(self):
        print("Resume Btn Clicked")

    def on_abortBtn1_clicked(self):
        print("Abort Btn Clicked")

    def on_restartBtn1_clicked(self):
        print("Restart Btn Clicked")

    def on_backBtn1_clicked(self):
        print("back Btn Clicked")

    def addLineToFileDisplay(self,line):
        self.fileDisplay.addItem(line)

def window():
    app = QApplication(sys.argv)
    w = MainScreen()
    w.show()
    sys.exit(app.exec_())
#if __name__ == '__main__':
window()
