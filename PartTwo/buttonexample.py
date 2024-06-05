import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,400)
        self.setWindowTitle("CVC Components Ltd")
        self.setWindowIcon(QIcon('images/cvc.jpg'))

        self.create_button()

    def create_button(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(100,100,130,130)
        btn.setFont(QFont("Times", 14, QFont.Weight.Bold))
        btn.setIcon(QIcon("images/cvc.jpg"))
        btn.setIconSize(QSize(50,50))

        #popup menu
        menu = QMenu()
        menu.setFont(QFont("Times", 14, QFont.Weight.Bold))
        menu.setStyleSheet("background-color:green")
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())