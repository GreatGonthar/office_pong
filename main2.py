''' Версия где мы заменяем глобальные переменные на классы'''

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
ui.alien_buttons(MainWindow)

MainWindow.show()

# логика
pad = 0
x_pole_min = 25 #размеры поля
x_pole_max = 432+8 
y_pole_min = 30
y_pole_max = 420

def slider_val():
	global pad 
	pad = int(ui.horizontalScrollBar.value()*7.5)

class MyBall:
	def __init__(self):
		self.x_ball = 100
		self.y_ball = 200
		self.size_ball = 16
		self.speed_x = 3
		self.speed_y = 3 

	def alien_show(self):
		self.row_and_column = ui.alien_column * ui.alien_row

		for i in range(self.row_and_column):
			
			if self.x_ball > ui.bx[i] - self.size_ball and \
		 		self.y_ball > ui.by[i] - self.size_ball and \
				self.x_ball < ui.bx[i] + ui.alien_size_x and \
				self.y_ball < ui.by[i] + ui.alien_size_y:
				# комета
				#ui.a[i].setDisabled(True)
				#ui.bx[i] = 0
				#ui.by[i] = 0
				if self.x_ball > ui.bx[i] - self.size_ball + 4 and self.x_ball < ui.bx[i] + ui.alien_size_x - 4:
					self.speed_y = -self.speed_y	
								
				if self.y_ball > ui.by[i] - self.size_ball + 4 and self.y_ball < ui.by[i] + ui.alien_size_y - 4:
					self.speed_x = -self.speed_x
				ui.bx[i] = 0
				ui.by[i] = 0
				ui.a[i].hide() #setDisabled(True) скрытый или невидимый
				
				
				
			

	def move(self):
		self.x_ball += self.speed_x
		self.y_ball += self.speed_y

		if self.x_ball >= x_pole_max or self.x_ball <= x_pole_min: #здесь мы отбиваемся от стен
			self.speed_x = -self.speed_x
		if self.y_ball >= y_pole_max - self.size_ball or self.y_ball <= y_pole_min:
			self.speed_y = -self.speed_y

		if self.y_ball >= 330 and self.y_ball <= 335: 
			if self.x_ball >= pad and self.x_ball <= pad + 90: # '90' это длинна нашей ракетки в пикселях
				if self.speed_y > 0: 
					self.speed_y = -self.speed_y
					if self.speed_y == -3: 
						self.speed_x = random.randrange(-1, 2, 2) * random.randrange(1, 4)
					if self.speed_x == 3 or self.speed_x == -3:
						self.speed_y = random.randrange(-3, 0)	
					print (self.speed_x, self.speed_y)
					print('revers()')	

	def show(self):		
		self.move()	
		self.alien_show()
		slider_val()
		ui.Ball.setGeometry(QtCore.QRect(self.x_ball, self.y_ball, self.size_ball, self.size_ball)) # отображаем шарик с переменными координатами
		ui.Ball.setText("😊")
		if self.y_ball > 331:
			ui.Ball.setText("😎")		
		if self.y_ball > 300 and self.y_ball < 330: #показываем эмоцию
			if self.x_ball >= pad and self.x_ball <= pad + 90 and self.speed_y < 0:
				ui.Ball.setText("😩")	
				

loop = MyBall() # TODO: сделать возможность одновременного появления нескольких шариков
iop = MyBall()
iop2 = MyBall()
def onTimeout():
	global iop, iop2
	iop.speed_y = 20
	loop.show()
	
	#loop2.show()
timer = QTimer()
timer.start(20)
timer.timeout.connect(onTimeout)

sys.exit(app.exec_())


   
    


    
