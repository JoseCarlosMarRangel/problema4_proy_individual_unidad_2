from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import sys


class Example(QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.flag = False
        self.ListaPuntos=[] 


    def initUI(self): #Aqui se muestra los botones y el label
    
        #self.setMouseTracking(True)
    
        self.setFixedSize(640, 480)
        self.setWindowTitle('Colours')
        self.btn = QPushButton("Paint", self)
        self.btn.move(540, 380)
        #self.btn.clicked.connect(self.onClicked)
        self.onClicked()
        self.show()
        
        self.qp = QPainter()


    def onClicked(self):
        self.flag = True
        self.update()


    def paintEvent(self, e):
        #if self.flag:
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawRectangles(self.qp)
        self.drawCircles(self.qp)
        print (self.ListaPuntos)
        for L in self.ListaPuntos:
            #print (L)
            pen = QtGui.QPen()
            pen.setWidth(5)
            pen.setColor(Qt.blue)
            self.qp.setPen(pen)
            #self.qp.setPen(Qt.blue)
            #self.qp.drawPoint(L[0], L[1])
            self.qp.drawEllipse(L[0], L[1], 35, 35)
        
        self.qp.end()


    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            x = e.x()
            y = e.y()
            text = f'x: {x},  y: {y}'
            #self.label.setText(text)
            print (x,y)
            self.ListaPuntos.append([x,y])
            self.update()
            #self.qp.setPen(Qt.red)
            #self.qp.drawPoint(x, y)


    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()
        text = f'x: {x},  y: {y}'
        #self.label.setText(text)
        print (x,y)
        
        
        




    def drawRectangles(self, qp):
        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(10, 15, 90, 60)
        
    def drawCircles(self, qp):        
        col = QColor(0, 0, 0)
        qp.setPen(col)
        qp.drawEllipse(200, 100, 70, 70)
        
        
if __name__ == '__main__':
    #Variable1=input ("Ingrese Variable1")
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())