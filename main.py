import sys
from random import randint, choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QPen, QPolygon
from PyQt5.QtCore import QPoint
from PyQt5 import uic


class Focus(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('knopochka.ui', self)
        self.initUI()
        self.qp = QPainter()

    def initUI(self):
        self.setWindowTitle('Кружочки')
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a=randint(5,100)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(randint(0,500), randint(0,500-a), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Focus()
    ex.show()
    sys.exit(app.exec_())
