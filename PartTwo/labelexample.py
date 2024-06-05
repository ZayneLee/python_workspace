from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,700,400)
        self.setWindowTitle("CVC Components Ltd")
        self.setWindowIcon(QIcon('images/cvc.jpg'))

        '''
        label = QLabel("Dash board", self)
        label.move(100,100)
        label.setFont(QFont("Sanserif",20))
        label.setStyleSheet("color:red")

        label = QLabel(self)
        pixmap = QPixmap('images/cvc.jpg')
        label.setPixmap(pixmap)
        '''

        label = QLabel(self)
        movie = QMovie('images/earth.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()



app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())