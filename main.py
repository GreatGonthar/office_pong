from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QScrollBar
from PyQt5.QtCore import QTimer
import sys
from pongGUI import Ui_MainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush


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
a=1 # переменные для реверса полета шарика
b=1
x_pole_min = 25 #размеры поля
x_pole_max = 432 + (size_ball/2)
y_pole_min = 30
pad = 0
emo = 0
score = 0

def slider_val():
	global _ball, y_ball, a, b, x_pole_min, x_pole_max, pad
	pad = ui.horizontalScrollBar.value() 
	
	print (int(pad*7.5))



def onTimeout():
	
	'''эта функция полета шарика, и его отражения от стен '''
	global x_ball, y_ball, a, b, x_pole_min, x_pole_max, pad, emo

	if x_ball >= x_pole_max: #здесь мы отбиваемся от стен
		a=-1
	elif x_ball <= x_pole_min:
		a=1
	x_ball=x_ball+(1*a)

	if y_ball >= 400 - size_ball:
		b=-1
	elif y_ball <= y_pole_min:
		b=1
	y_ball=y_ball+(1*b)

	ui.Ball.setText("😊")

	if y_ball == 330: #здесь мы отбиваемся от ракетки
		if x_ball >= int(pad*7.5) and x_ball <= int(pad*7.5)+90:
			
			if b == 1:
				score_swith()	
			b = -1 			
	if y_ball > 331:
		ui.Ball.setText("😩")		

	if y_ball > 300 and y_ball < 330:
		if x_ball >= int(pad*7.5) and x_ball <= int(pad*7.5)+90 and b == -1:
			ui.Ball.setText("😎")	
	
	#print('----',x_ball, pad*7.5)

	ui.Ball.setGeometry(QtCore.QRect(x_ball, y_ball, size_ball, size_ball))

	

def score_swith():
	global score
	score +=100
	lable_text = str("Score: " + str(score))
	ui.label.setText(lable_text)
	print (lable_text)
	pass



	

timer = QTimer()
timer.timeout.connect(onTimeout)
timer.start(20)	


ui.horizontalScrollBar.sliderMoved.connect(slider_val)	


ui.Ball.clicked.connect(score_swith)


# запускаем главную петлю

sys.exit(app.exec_())


   
    


    
