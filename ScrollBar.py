import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QScrollBar
from PyQt5.QtGui import QPalette, QColor, QFont
'''меняем цвет скроллбаром '''

class ScrollBar(QWidget):

    def __init__(self, parent=None):
        super(ScrollBar, self).__init__(parent)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('ScrollBar')

        self.lbl = QLabel('Slide scrollbar to change color')
        self.lbl.setFont(QFont('Arial', 16))

        self.scrollbar1 = QScrollBar()
        self.scrollbar1.setMaximum(255)
        self.scrollbar1.sliderMoved.connect(self.slider_val)

        self.scrollbar2 = QScrollBar()
        self.scrollbar2.setMaximum(255)
        self.scrollbar2.sliderMoved.connect(self.slider_val)

        self.scrollbar3 = QScrollBar()
        self.scrollbar3.setMaximum(255)
        self.scrollbar3.sliderMoved.connect(self.slider_val)

        layout = QHBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.scrollbar1)
        layout.addWidget(self.scrollbar2)
        layout.addWidget(self.scrollbar3)
        self.setLayout(layout)

    def slider_val(self):
        print(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value())
        palette = QPalette()
        color = QColor(self.scrollbar1.value(), self.scrollbar2.value(), self.scrollbar3.value(), 50)
        palette.setColor(QPalette.Foreground, color)
        self.lbl.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = ScrollBar()
    win.show()
    sys.exit(app.exec_())