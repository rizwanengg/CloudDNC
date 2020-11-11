import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

global xpixels
global ypixels

app1 = QtWidgets.QApplication(sys.argv)
screen = app1.primaryScreen()
size = screen.size()

xpixels = size.width()
ypixels = size.height()

class Ui_DNCLoggerMainScreen(object):
    def setupUi(self, DNCLoggerMainScreen):
        DNCLoggerMainScreen.setObjectName("DNCLoggerMainScreen")
        DNCLoggerMainScreen.setWindowModality(QtCore.Qt.WindowModal)
        #DNCLoggerMainScreen.resize(548, 250)
        DNCLoggerMainScreen.resize(xpixels, ypixels)

        DNCLoggerMainScreen.setWindowFlag(Qt.FramelessWindowHint)  # Change hide title bar

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DNCLoggerMainScreen.sizePolicy().hasHeightForWidth())
        DNCLoggerMainScreen.setSizePolicy(sizePolicy)
        DNCLoggerMainScreen.setMinimumSize(QtCore.QSize(0, 250))
        DNCLoggerMainScreen.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../.designer/GUIPractice/n-c-tools-120x120.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DNCLoggerMainScreen.setWindowIcon(icon)
        DNCLoggerMainScreen.setInputMethodHints(QtCore.Qt.ImhNoEditMenu)
        DNCLoggerMainScreen.setTabShape(QtWidgets.QTabWidget.Triangular)
        DNCLoggerMainScreen.setDockNestingEnabled(False)
        DNCLoggerMainScreen.setProperty("flag", "")
        self.centralwidget = QtWidgets.QWidget(DNCLoggerMainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendBtn.sizePolicy().hasHeightForWidth())
        self.sendBtn.setSizePolicy(sizePolicy)
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout.addWidget(self.sendBtn)
        self.pauseBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pauseBtn.sizePolicy().hasHeightForWidth())
        self.pauseBtn.setSizePolicy(sizePolicy)
        self.pauseBtn.setObjectName("pauseBtn")
        self.horizontalLayout.addWidget(self.pauseBtn)
        self.resumeBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resumeBtn.sizePolicy().hasHeightForWidth())
        self.resumeBtn.setSizePolicy(sizePolicy)
        self.resumeBtn.setObjectName("resumeBtn")
        self.horizontalLayout.addWidget(self.resumeBtn)
        self.abortBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.abortBtn.sizePolicy().hasHeightForWidth())
        self.abortBtn.setSizePolicy(sizePolicy)
        self.abortBtn.setObjectName("abortBtn")
        self.horizontalLayout.addWidget(self.abortBtn)
        self.restartBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.restartBtn.sizePolicy().hasHeightForWidth())
        self.restartBtn.setSizePolicy(sizePolicy)
        self.restartBtn.setObjectName("restartBtn")
        self.horizontalLayout.addWidget(self.restartBtn)
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backBtn.sizePolicy().hasHeightForWidth())
        self.backBtn.setSizePolicy(sizePolicy)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 2)
        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setMouseTracking(False)
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.gridLayout.addWidget(self.progress, 4, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fileDisplay = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileDisplay.sizePolicy().hasHeightForWidth())
        self.fileDisplay.setSizePolicy(sizePolicy)
        self.fileDisplay.setMinimumSize(QtCore.QSize(350, 0))
        self.fileDisplay.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.fileDisplay.setAlternatingRowColors(True)
        self.fileDisplay.setModelColumn(0)
        self.fileDisplay.setObjectName("fileDisplay")
        self.horizontalLayout_2.addWidget(self.fileDisplay)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblTool = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTool.sizePolicy().hasHeightForWidth())
        self.lblTool.setSizePolicy(sizePolicy)
        self.lblTool.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblTool.setObjectName("lblTool")
        self.gridLayout_2.addWidget(self.lblTool, 2, 1, 1, 1)
        self.lblFeed = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFeed.sizePolicy().hasHeightForWidth())
        self.lblFeed.setSizePolicy(sizePolicy)
        self.lblFeed.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblFeed.setObjectName("lblFeed")
        self.gridLayout_2.addWidget(self.lblFeed, 0, 1, 1, 1)
        self.lblWork = QtWidgets.QLabel(self.centralwidget)
        self.lblWork.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblWork.setObjectName("lblWork")
        self.gridLayout_2.addWidget(self.lblWork, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.lblRPM = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblRPM.sizePolicy().hasHeightForWidth())
        self.lblRPM.setSizePolicy(sizePolicy)
        self.lblRPM.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lblRPM.setObjectName("lblRPM")
        self.gridLayout_2.addWidget(self.lblRPM, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_2.addWidget(self.line_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.lblHOff = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblHOff.sizePolicy().hasHeightForWidth())
        self.lblHOff.setSizePolicy(sizePolicy)
        self.lblHOff.setObjectName("lblHOff")
        self.gridLayout_3.addWidget(self.lblHOff, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)
        self.lblZL = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblZL.sizePolicy().hasHeightForWidth())
        self.lblZL.setSizePolicy(sizePolicy)
        self.lblZL.setObjectName("lblZL")
        self.gridLayout_3.addWidget(self.lblZL, 2, 1, 1, 1)
        self.lblZH = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblZH.sizePolicy().hasHeightForWidth())
        self.lblZH.setSizePolicy(sizePolicy)
        self.lblZH.setObjectName("lblZH")
        self.gridLayout_3.addWidget(self.lblZH, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.lblTotTime = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTotTime.sizePolicy().hasHeightForWidth())
        self.lblTotTime.setSizePolicy(sizePolicy)
        self.lblTotTime.setObjectName("lblTotTime")
        self.gridLayout_3.addWidget(self.lblTotTime, 3, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 3, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_3)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_2.addWidget(self.line_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setMidLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        DNCLoggerMainScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DNCLoggerMainScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 21))
        self.menubar.setObjectName("menubar")
        DNCLoggerMainScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DNCLoggerMainScreen)
        self.statusbar.setObjectName("statusbar")
        DNCLoggerMainScreen.setStatusBar(self.statusbar)

        self.retranslateUi(DNCLoggerMainScreen)
        QtCore.QMetaObject.connectSlotsByName(DNCLoggerMainScreen)

    def retranslateUi(self, DNCLoggerMainScreen):
        _translate = QtCore.QCoreApplication.translate
        DNCLoggerMainScreen.setWindowTitle(_translate("DNCLoggerMainScreen", "Nectar DNC Logger"))
        self.sendBtn.setText(_translate("DNCLoggerMainScreen", "Send"))
        self.pauseBtn.setText(_translate("DNCLoggerMainScreen", "Pause"))
        self.resumeBtn.setText(_translate("DNCLoggerMainScreen", "Resume"))
        self.abortBtn.setText(_translate("DNCLoggerMainScreen", "Abort"))
        self.restartBtn.setText(_translate("DNCLoggerMainScreen", "Restart"))
        self.backBtn.setText(_translate("DNCLoggerMainScreen", "Back"))
        self.label.setText(_translate("DNCLoggerMainScreen", "File upload status:"))
        self.lblTool.setText(_translate("DNCLoggerMainScreen", "NA"))
        self.lblFeed.setText(_translate("DNCLoggerMainScreen", "NA"))
        self.lblWork.setText(_translate("DNCLoggerMainScreen", "Work"))
        self.label_6.setText(_translate("DNCLoggerMainScreen", "RPM"))
        self.lblRPM.setText(_translate("DNCLoggerMainScreen", "NA"))
        self.label_4.setText(_translate("DNCLoggerMainScreen", "Tool No."))
        self.label_9.setText(_translate("DNCLoggerMainScreen", "NA"))
        self.label_3.setText(_translate("DNCLoggerMainScreen", "Feed"))
        self.label_11.setText(_translate("DNCLoggerMainScreen", "H-Offset"))
        self.lblHOff.setText(_translate("DNCLoggerMainScreen", "NA"))
        self.label_14.setText(_translate("DNCLoggerMainScreen", "Z-Low"))
        self.lblZL.setText(_translate("DNCLoggerMainScreen", "NA"))
        self.lblZH.setText(_translate("DNCLoggerMainScreen", "NA"))
        self.label_10.setText(_translate("DNCLoggerMainScreen", "Z-High"))
        self.lblTotTime.setText(_translate("DNCLoggerMainScreen", "NA"))
        self.label_16.setText(_translate("DNCLoggerMainScreen", "Total Time"))
        self.label_2.setText(_translate("DNCLoggerMainScreen", "Nectar DNC Logger"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    DNCLoggerMainScreen = QtWidgets.QMainWindow()
    # ------------------modification-----------------
    screen = app.primaryScreen()
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    xpixels = size.width()
    ypixels = size.height()
    # ------------------modification-----------------

    ui = Ui_DNCLoggerMainScreen()
    ui.setupUi(DNCLoggerMainScreen)
    DNCLoggerMainScreen.show()
    sys.exit(app.exec_())
