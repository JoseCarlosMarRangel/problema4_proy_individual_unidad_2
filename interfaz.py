
from PyQt5 import QtGui

from PyQt5.QtWidgets import *

from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5 import *


class gui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setFixedSize(640, 480)
        self.setWindowTitle('Colours')
        self.btn = QPushButton("Paint", self)
        self.btn.move(540, 380)
        self.btn.clicked.connect(self.onClicked)
        self.show()

        self.qp = QPainter()

    def onClicked(self):
        self.flag = True
        self.update()

    def paintEvent(self, e):
        # if self.flag:
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawRectangles(self.qp)
        self.drawCircles(self.qp)
        print(self.ListaPuntos)
        for L in self.ListaPuntos:
            #print (L)
            pen = QtGui.QPen()
            pen.setWidth(5)
            pen.setColor(Qt.blue)
            self.qp.setPen(pen)
            # self.qp.setPen(Qt.blue)
            self.qp.drawPoint(L[0], L[1])

        self.qp.end()
