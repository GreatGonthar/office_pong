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
score = 0
pad = 0

def slider_val():
	global pad 
	pad = ui.horizontalScrollBar.value() 
	
def onTimeout():
	
	'''эта функция полета шарика, и его отражения от стен '''

	global x_ball, y_ball, a, b, x_pole_min, x_pole_max, pad
	
	ui.Ball.setGeometry(QtCore.QRect(x_ball, y_ball, size_ball, size_ball)) # отображаем шарик с переменными координатами
	ui.Ball.setText("😊")
	x_ball += a
	y_ball += b
	
	if x_ball >= x_pole_max or x_ball <= x_pole_min: #здесь мы отбиваемся от стен
		a = -a
		
	if y_ball >= y_pole_max - size_ball or y_ball <= y_pole_min:
		b = -b	

	if y_ball >= 330 and y_ball <= 335: #здесь мы отбиваемся от ракетки
		if x_ball >= int(pad*7.5) and x_ball <= int(pad*7.5)+90: # '90' это длинна нашей ракетки в пикселях
			if b > 0: # если шарик летит вниз добавляем очки
				score_swith()	
	
	if y_ball > 331:
		ui.Ball.setText("😎")		

	if y_ball > 300 and y_ball < 330: #показываем эмоцию
		if x_ball >= int(pad*7.5) and x_ball <= int(pad*7.5)+90 and b < 0:
			ui.Ball.setText("😩")			
	
	if x_ball > 40 and x_ball < 90 and y_ball > 80-size_ball and y_ball < 105: # TOODO: пытаемся отразится от кнопки
		a=-a
		print (x_ball,y_ball)

def score_swith():
	''' набираем очки'''
	global score, b, a
	score +=100
	lable_text = str("Score: " + str(score))
	ui.label.setText(lable_text)
	print (lable_text)
	''' скорость по одной из осей должна всегда быть три (для равномерного движения)'''
	if b == 3 or b == -3: 
		a = random.randrange(-1, 2, 2) * random.randrange(1, 4)
	if a == 3 or a == -3:
		b = random.randrange(1, 4)	
	print (a, b)
	b = -b # шарик летит вверх после отбивания

def aliens():
	#ui.Button1.show()
	#ui.Button1.hide()
	print('hallo')

timer = QTimer()
timer.start(20)
timer.timeout.connect(onTimeout)

ui.horizontalScrollBar.sliderMoved.connect(slider_val)	

ui.Button2.clicked.connect(aliens)

# запускаем главную петлю

sys.exit(app.exec_())


   
    


    
