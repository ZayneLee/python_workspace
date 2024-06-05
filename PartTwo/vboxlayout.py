import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QHBoxLayout")
        self.setWindowIcon(QIcon('images/cvc.jpg'))

        vbox = QVBoxLayout()

        btn1 = QPushButton("One")
        btn2 = QPushButton("Two")
        btn3 = QPushButton("Three")
        btn4 = QPushButton("Four")

        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        # vbox.addSpacing(100)
        vbox.addStretch(5)

        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
