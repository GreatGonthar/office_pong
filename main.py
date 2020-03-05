''' Версия где мы заменяем глобальные переменные на классы'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox
#from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QScrollBar
from PyQt5.QtCore import QTimer, Qt
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
x_pole_max = 432+7
y_pole_min = 30
y_pole_max = 420

def slider_val():
	global pad 
	pad = int(ui.horizontalScrollBar.value()*7.5)

class MyBall:
	def __init__(self):
		self.x_ball = 50
		self.y_ball = 400
		self.size_ball = 16
		self.speed_x = 1
		self.speed_y = -3 
		self.score = 0

	def alien_show(self):
		self.row_and_column = ui.alien_column * ui.alien_row
		
		for i in range(self.row_and_column): #создаем цикл появления пришельцев, кол-во итераций равно их количеству

			ui.a[i].setText(str(ui.alien_type[i])) #меняем текст на кнопке-пришельце на номер(тип нашего пришельца)
			alien_clr = str(ui.alien_type[i]/20) #задаем степень прозрачности пришельца, в зависимости от числа его типа
			# css стиль кнопки пришельца (задаем цвет кнопки)
			ui.a[i].setStyleSheet('QPushButton {background-color: rgba(10,10,10,'+alien_clr+'); border-style: solid; border-width: 1px; border-color: gray; color: black; }')
			
			if ui.alien_type[i] == 0: # если тип пришельца(его число) меньше нуля, то 					
					ui.a[i].hide() # и делаем его невидимым (setDisabled(True) скрытый или невидимый)

			if self.y_ball >= y_pole_max - self.size_ball: #если мячик достигает дна
				ui.alien_type[i] += 1 #прибавляем по единице всем пришельцам
				ui.a[i].show() #и отображаем тех кто был скрыт
				#ui.bx[i], ui.by[i] = ui.b[i]

			if self.x_ball > ui.bx[i] - self.size_ball and \
		 		self.y_ball > ui.by[i] - self.size_ball and \
				self.x_ball < ui.bx[i] + ui.alien_size_x and \
				self.y_ball < ui.by[i] + ui.alien_size_y and ui.alien_type[i] > 0: # номер пришельца больше нуля, значит он существует
				'''условие отбивания от пришельцааааааааааааааааааааааааааааааааа'''	 

				ui.alien_type[i] -= 1
				# пока не используемая функция кометы
				#ui.a[i].setDisabled(True)
				#ui.bx[i] = 0
				#ui.by[i] = 0
				

				if self.x_ball > ui.bx[i] - self.size_ball + 4 and self.x_ball < ui.bx[i] + ui.alien_size_x - 4:
					self.speed_y = -self.speed_y # в зависимости с какой стороны пришельца шарик подлетел, делаем его реверс
					#ui.alien_type[i] -= 1
			
				if self.y_ball > ui.by[i] - self.size_ball + 4 and self.y_ball < ui.by[i] + ui.alien_size_y - 4:
					self.speed_x = -self.speed_x
					#ui.alien_type[i] -= 1


					# если у пришельца цифра больше нуля, то отнимаем одну единичку (после удара мячиком конечно)					
				self.score += 100
				ui.label.setText(("Score: " + str(self.score))) #отображаем очки
				self.dialog_message()

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
	
	def dialog_message(self):
		message = QMessageBox.question(MainWindow, 'Победа !!!', "Еще разок?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
		if message == QMessageBox.No:
			message2 = QMessageBox.question(MainWindow, '😊😊😊',"Ты уверен?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)			
			if message2 == QMessageBox.Yes:
			
				message3 = QMessageBox.question(MainWindow, '😎😎😎',"Точно уверен?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
				if message3 == QMessageBox.Yes:   
					QMessageBox.information(MainWindow, '😩😩😩',"Ну ладно \n 😩😩😩", QMessageBox.Ok, QMessageBox.Ok)
					sys.exit(app.exec_())              
				else:
					ui.setupUi(MainWindow)
					ui.alien_buttons(MainWindow)
					self.__init__()	
			else:
				ui.setupUi(MainWindow)
				ui.alien_buttons(MainWindow)
				self.__init__()
		else:
			ui.setupUi(MainWindow)
			ui.alien_buttons(MainWindow)
			self.__init__()
            	
				

loop = MyBall() # TODO: сделать возможность одновременного появления нескольких шариков

def onTimeout():

	loop.show()
	
	#loop2.show()
timer = QTimer()
timer.start(20)
timer.timeout.connect(onTimeout)

sys.exit(app.exec_())


   
    


    
