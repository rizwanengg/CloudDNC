import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


def showdialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)

    msg.setText("This is a message box")
    msg.setInformativeText("This is additional information")
    msg.setWindowTitle("MessageBox demo")
    msg.setDetailedText("The details are as follows:")
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.buttonClicked.connect(msgbtn)

    retval = msg.exec_()
    print("value of pressed message box button:", retval)

def msgbtn(i):
    print
    "Button pressed is:", i.text()


