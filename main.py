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

# логика
size_ball = 16
x_ball = 260 # начальные координаты шарика (45 - самый левый край ракетки, 420 - самый правый край ракетки) 48 - длинна ракетки
y_ball = 130 # (325 - самый низ ракетки)
a=3 # переменные для реверса полета шарика
b=3
x_pole_min = 25 #размеры поля
x_pole_max = 432 + (size_ball/2)
y_pole_min = 30
y_pole_max = 420
pad = 0
emo = 0
score = 0
directionx = 0
directiony = 0
rndx = 1
rndy = 1


def slider_val():
	global _ball, y_ball, a, b, x_pole_min, x_pole_max, pad
	pad = ui.horizontalScrollBar.value() 
	
	#print (int(pad*7.5))



def onTimeout():
	
	'''эта функция полета шарика, и его отражения от стен '''

	global x_ball, y_ball, a, b, x_pole_min, x_pole_max, pad, emo, directionx, directiony, rndx, rndy

	if directionx <= 0:
		if x_ball >= x_pole_max or x_ball <= x_pole_min: #здесь мы отбиваемся от стен
			a = -a
		x_ball = x_ball + (a) #движение шарика по осям на '1' пиксель
	
	
	if directiony <= 0:
		if y_ball >= y_pole_max - size_ball or y_ball <= y_pole_min:
			b = -b
		y_ball = y_ball + (b)

	ui.Ball.setText("😊")

	if y_ball >= 330 and y_ball <= 335: #здесь мы отбиваемся от ракетки
		if x_ball >= int(pad*7.5) and x_ball <= int(pad*7.5)+90: # '90' это длинна нашей ракетки в пикселях
			
			if b > 0: # если шарик летит вниз добавляем очки
				score_swith()	
			
			
			
	if y_ball > 331:
		ui.Ball.setText("😩")		

	if y_ball > 300 and y_ball < 330: #показываем эмоцию
		if x_ball >= int(pad*7.5) and x_ball <= int(pad*7.5)+90 and b == -1:
			ui.Ball.setText("😎")	
	
	#print('----',x_ball, pad*7.5)
	

	directionx -= 1
	if directionx < 0:
		directionx = rndx 
	
	directiony -= 1
	if directiony < 0:
		directiony = rndy 
		


	ui.Ball.setGeometry(QtCore.QRect(x_ball, y_ball, size_ball, size_ball)) # отображаем шарик с переменными координатами
	#print (directionx, directiony)
	

def score_swith():
	global score, b, a
	score +=100
	lable_text = str("Score: " + str(score))
	ui.label.setText(lable_text)
	print (lable_text)
	if b == 3 or b == -3:
		a = random.randrange(-1, 2, 2) * random.randrange(1, 4)
	if a == 3 or a == -3:
		b = random.randrange(1, 4)
	
	print (a, b)
	b = -b # шарик летит вверх после отбивания

def def_a():
	global a
	a += 1
	print (a, b)

def def_b():
	global b
	b += 1
	print (a, b)	

timer = QTimer()
timer.start(10)
timer.timeout.connect(onTimeout)

	


ui.horizontalScrollBar.sliderMoved.connect(slider_val)	


ui.Button1.clicked.connect(def_a)
ui.Button2.clicked.connect(def_b)


# запускаем главную петлю

sys.exit(app.exec_())


   
    


    
