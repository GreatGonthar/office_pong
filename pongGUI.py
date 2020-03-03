# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pongGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 450)
        MainWindow.setMinimumSize(482, 440)
        MainWindow.setMaximumSize(482, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(25, 30, 432, 390))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(30, 340, 421, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setSizeIncrement(QtCore.QSize(0, 0))
        self.horizontalScrollBar.setMouseTracking(True)
        self.horizontalScrollBar.setTabletTracking(True)
        self.horizontalScrollBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.horizontalScrollBar.setMinimum(0)
        self.horizontalScrollBar.setMaximum(50)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        

        #self.Ball.setObjectName("Ball")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 2))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 5, 131, 21))
        self.label.setObjectName("label")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)    

    def alien_buttons(self, MainWindow):

        
        self.a = [] #массив экземпляров кнопки
        self.bx = [] #массив координат кнопки x
        self.by = [] #массив координат кнопки y
        self.b = []
        self.alien_type = []
        self.unit = 0
        #self.step_x = 0
        self.step_y = 100
        self.alien_size_x = 50
        self.alien_size_y = 25
        self.alien_column = 7
        self.alien_row = 4
   
        for i in range(self.alien_row):
            self.step_y += self.alien_size_y
            self.step_x = self.alien_size_x
            
            for j in range(self.alien_column):
                
                self.a.append(QtWidgets.QPushButton('iop', self.centralwidget))    

                self.a[self.unit].setGeometry(QtCore.QRect(self.step_x, self.step_y, self.alien_size_x, self.alien_size_y))  
                
                self.b.append((self.step_x, self.step_y))
                self.bx.append(self.step_x)
                self.by.append(self.step_y) 
                self.unit += 1                   
                self.step_x += self.alien_size_x
                self.alien_type.append(random.randrange(0, 5))
        self.Ball = QtWidgets.QPushButton(self.centralwidget)
        self.Ball.setGeometry(QtCore.QRect(260, 130, 16, 16))
        self.Ball.setStyleSheet('background: black;')


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "-= 🏓Office PONG🎾 =-"))
        #self.Ball.setText(_translate("MainWindow", "😊"))
        self.label.setText(_translate("MainWindow", "Score: 0"))
    


