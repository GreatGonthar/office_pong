from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QScrollBar
from PyQt5.QtCore import QTimer
import sys
from pongGUI import Ui_MainWindow


# создание приложения
app = QtWidgets.QApplication(sys.argv)

# создаем форму, и инициализируем UI
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# логика
x_ball = 260
y_ball = 130
a=1
b=1
def onTimeout():
	global x_ball, y_ball, a, b
	if x_ball >= 500-16:
		a=-1
	elif x_ball <= 0:
		a=1
	x_ball=x_ball+(1*a)

	if y_ball >= 400-16:
		b=-1
	elif y_ball <= 0:
		b=1
	y_ball=y_ball+(1*b)
	
	print(x_ball, y_ball)

	ui.Ball.setGeometry(QtCore.QRect(x_ball, y_ball, 16, 16))
	

def doAction():
	pass


def slider_val():
	global x, y
	x_move = ui.horizontalScrollBar.value() 
	


timer = QTimer()
timer.timeout.connect(onTimeout)
timer.start(30)	

ui.horizontalScrollBar.sliderMoved.connect(slider_val)	


ui.Ball.clicked.connect(doAction)


# запускаем главную петлю

sys.exit(app.exec_())


   
    


    
