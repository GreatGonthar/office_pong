

#Пример того, как заменить глобальные переменные классами

from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QScrollBar
from PyQt5.QtCore import QTimer
import sys
from pongGUI import Ui_MainWindow
#from PyQt5.QtGui import QPainter, QColor, QBrush
import random


# создание приложения
app = QtWidgets.QApplication(sys.argv)

# создаем форму, и инициализируем UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

class Pr:
	def __init__(self):
		self.x = 100
		self.y = 100
		self.dx = +5

	def move(self):
		self.x += self.dx
		self.y -= self.dx
				
	def show(self):		
		self.move()
		print(self.x, self.y)

loop = Pr()
def onTimeout():
	global loop
	loop.show()
	
	
timer = QTimer()
timer.start(1000)
timer.timeout.connect(onTimeout)

sys.exit(app.exec_())

