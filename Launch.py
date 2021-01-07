import tkinter as tk
from os import listdir
from os.path import isfile, join
from ReadJSON import *
#from Launch import fname


import threading
import sys
from PyQt5 import QtWidgets

#import easygui
import serial
from PyQt5.QtWidgets import QMessageBox

from LocalFileRead import openFile
from MachineFileRead import readFileFromMachine
from MainScreen import Ui_DNCLoggerMainScreen
#from getFilename import browseFile
global fname
#python -m PyQt5.uic.pyuic -x MainScreen.ui -o MainScreen.py

from ReadJSON import *
from SerialPortFunc import detectPort, openPort

try:
    # ser = openPort(selectPort(), 9600, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
    ser = openPort(getPortNo(), getBrate(), serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE)
    ser.xonxoff = True

except:
    print("Line 24: " + IOError)

ReadThread = threading.Thread(target=readFileFromMachine, args=(ser,))
ReadThread.start()
print("Machine to Device File Reading active.")

def browseFile():
    mypath=getFolderURL()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    #print (onlyfiles)

    window_main = tk.Tk(className='Select File to Send.')
    window_main.geometry('250x250')
     
    listbox_1 = tk.Listbox(window_main, selectmode=tk.EXTENDED)
    i=1
    for item in onlyfiles:
        
        listbox_1.insert(i, item)
        i=i+1

    listbox_1.pack()
     
    def submitFunction():
        selection = listbox_1.curselection()
        data = listbox_1.get(selection)

        print('Data is:',data)
        fileptr1 = open("CurrentFileRead.txt", "w")
        fileptr1.write(data)
        fileptr1.close()
        window_main.destroy()
        #return data
     
    submit = tk.Button(window_main, text='OK', command=submitFunction)
    submit.pack()
   # cancelq = tk.Button(window_main, text='Cancel', command=window_main.destroy())
   # cancelq.pack()

    window_main.mainloop()
    
#browseFile()
    

class MainScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.ui = Ui_DNCLoggerMainScreen()
        self.ui.setupUi(self)
        #self.ui.DNCLoggerMainScreen.resize(1024, 768)
        #self.ui.progress.setValue(0)

        self.ui.sendBtn.clicked.connect(self.on_sendBtn1_clicked)
        self.ui.pauseBtn.clicked.connect(self.on_pauseBtn1_clicked)
        self.ui.resumeBtn.clicked.connect(self.on_resumeBtn1_clicked)
        self.ui.abortBtn.clicked.connect(self.on_abortBtn1_clicked)
        self.ui.restartBtn.clicked.connect(self.on_restartBtn1_clicked)
        self.ui.backBtn.clicked.connect(self.on_backBtn1_clicked)


    def on_sendBtn1_clicked(self):
        print("Send Btn Clicked")
        file_path_string = ""
        try:
            self.displayFile()
        except(IOError,Exception):
            print(Exception)

    def displayFile(self):
    #    print(getFolderURL())

        try:
            browseFile()
            fileptr1 = open("CurrentFileRead.txt", "r")
            faname=fileptr1.read()
            fileptr1.close()
            print(faname)
            file_path_string = getFolderURL()+faname
            #file_path_string = easygui.fileopenbox(msg="Select single file at a time.", title="Choose",default=getFolderURL(),filetypes=None, multiple=False)
            #file_path_string = filedialog.askopenfilename(initialdir =  getFolderURL(), title = "Select A File", filetype = (("all files","*.*")) )
        
     #   file_path_string = (file_path_string.replace('\\', "/"))
     #   x = file_path_string.split("/")
       # l = len(x)
        
    #    file_path = getFolderURL()+x[l - 1]
            print(file_path_string)
        except:
            print("File browse error.")
        #print(getPortNo(), getBrate(), getDataBits(), getParity(), getStopBits())
     #   detectPort()
        total_Lines = self.countLinesInFile(file_path_string)#pi
        print(total_Lines)
        
        fileptr = open(file_path_string, "r")#pi
        
            
        try:
            #_thread.start_new_thread(self.sendFile1,ser,fileptr, (x))

            Th = threading.Thread(target=self.sendFile1, args=(ser,fileptr,total_Lines))
            Th.start()

        except:
            QMessageBox.information(self, "File Send Thread Error",)

    def countLinesInFile(self,filename):
        file = openFile(filename)
        Counter = 0
        Content = file.read()
        CoList = Content.split("\n")

        for i in CoList:
            if i:
                Counter += 1
        file.close()
        return Counter

    def sendFile1(self,ser,fileptr1,totLines):
        lineno = 0
    #    self.ui.progress.setValue(0)
        #x = totLines
        #y = 100 / x

        while True:
            line = fileptr1.readline()
        #    QMessageBox.information(self, "Info", line)
            lineno += 1
            if not line:
                break
            self.split_to_char(ser,line)

            full_line = "{}".format(lineno) + "  " + line.strip()
            self.addLineToFileDisplay(full_line,lineno)

           # y = int(y + round(100 / x))
           # print(y)
       #     self.ui.progress.setValue(y)       # setting value to progress bar


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

    def addLineToFileDisplay(self,line,lineno):
        self.ui.fileDisplay.addItem(line)
        #self.ui.progress.setValue(lineno)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainScreen()
    window.show()
    sys.exit(app.exec_())