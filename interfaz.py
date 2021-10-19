
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *


class gui(QWidget):

    listadepuntos = []

    def __init__(self):
        super().__init__()
        self.flag = False
        self.flag1 = False
        self.dibujar = False
        self.Listadepuntos = []
        self.x
        self.y
        self.initUI()

    def initUI(self):
        self.setFixedSize(640, 480)
        self.setWindowTitle('Grafos no dirigidos')
        
        self.btn1 = QPushButton('Circulo',self)
        self.btn1.move(540, 380)
        self.btn1.clicked.connect(self.onClicked1)
        
        self.btn2 = QPushButton('Linea',self)
        self.btn2.move(540, 410)
        self.btn2.clicked.connect(self.onClicked2)
        
        self.btn3 = QPushButton('Limpiar',self)
        self.btn3.move(540, 440)
        self.btn3.clicked.connect(self.borrardibujos)
        
        self.show()
        self.qp = QPainter()

    def onClicked1(self):
        self.dibujar = True
        self.flag = True
        self.update()

    def onClicked2(self):
        self.dibujar = True
        self.flag1 = True
        self.update()
        

    
    def paintEvent(self, e):
        self.qp = QPainter()
        self.qp.begin(self)
        self.contador = 0
        
        if self.flag == True:
            self.dibujarcirculo(self.qp)
            self.flag = False
        if self.flag1 == True:
                self.dibujarlinea(self.qp)
                self.flag1 = False
        
        self.qp.end()
        
        
    def dibujarcirculo (self, qp): 
        for L in self.Listadepuntos:
            pen = QtGui.QPen()
            pen.setWidth(5)
            pen.setColor(Qt.blue)
            qp.setPen(pen)
            qp.drawEllipse(L[0], L[1], 35, 35)
            self.contador = self.contador + 1
            qp.drawText(L[0], L[1], str(self.contador))
        
    def dibujarlinea(self, qp):
        pen = QtGui.QPen()
        pen.setWidth(5)
        pen.setColor(Qt.blue)
        qp.setPen(pen)
        qp.drawLine(self.x, self.y, self.x, self.y)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.x = e.x()
            self.y = e.y()
            text = f'x: {self.x},  y: {self.y}'
            print (self.x,self.y)
            self.Listadepuntos.append([self.x,self.y])
            
    def mouseMoveEvent(self, e):
        self.x = e.x()
        self.y = e.y()
        text = f'x: {self.x},  y: {self.y}'
        print (self.x,self.y)

    def borrardibujos(self):
        self.Listadepuntos = []
        self.x = 0
        self.y = 0
        self.update()