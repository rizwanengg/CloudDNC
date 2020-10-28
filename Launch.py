import sys
import time
import easygui
import serial

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMessageBox, QMainWindow
from PyQt5.uic import loadUi
from SerialPortFunc import detectPort, openPort, selectPort, closePort
from ReadJSON import *
import tkinter as tk
from tkinter import filedialog
from MsgBox import showdialog
from LocalFileRead import openFile
#FILE_LIMIT = 100
#RATE_OF_CHANGE = 1

global ser_1

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
        print(getPortNo(), getBrate(), getDataBits(), getParity(), getStopBits())
        detectPort()
        ser_1 = openPort(getPortNo(), getBrate(),getDataBits(), getParity(), getStopBits())

        fileptr = open(file_path, "r")
        #self.countLines(file_path)
        lineno = 0;

        while True:
              line = fileptr.readline()
              QMessageBox.information(self, "Info", line)
              lineno += 1
              if not line:
                    break

              # selectPort()
#              self.split_to_char(line)
              ser_1.write(line.encode())

                #write code to send char over COM port here

            #  closePort(ser_1)

              fullline = "{}".format(lineno) + "  " + line.strip()
              self.addLineToFileDisplay(fullline)

            # showdialog()
        fileptr.close()
        closePort(ser_1)
        #except(Exception):
     #   print("Display file error")

    def split_to_char (self,word):
   #     print(word)
#        print (len(word))
        for x in range(len(word)):
            ch1=word[x]
            ser_1.write(ch1.encode())
            print(ch1)
        #return (word)

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
