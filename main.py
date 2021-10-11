"""
Creado con Python3 y PyQt5
Graficador de grafos no dirigidos
Creador: Jose Carlos Mar Rangel
"""

import sys # Para usar sys.exit()
from PyQt5.QtWidgets import QApplication
from interfaz import gui #gui de la interfaz

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = gui()
    sys.exit(app.exec_())