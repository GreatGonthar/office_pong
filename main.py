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
x = 260
y = 130

def onTimeout():
	global x, y
	x+=1
	print(x)
	ui.Ball.setGeometry(QtCore.QRect(x, y, 16, 16))


def doAction():
	pass


def slider_val():
	global x, y
	x_move = ui.horizontalScrollBar.value() 
	


timer = QTimer()
timer.timeout.connect(onTimeout)
timer.start(1000)	

ui.horizontalScrollBar.sliderMoved.connect(slider_val)	


ui.Ball.clicked.connect(doAction)


# запускаем главную петлю

sys.exit(app.exec_())


   
    


    
