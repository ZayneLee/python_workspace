import sys

from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QLineEdit")
        self.setWindowIcon(QIcon('images/cvc.jpg'))

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Sanserif", 15))
        # line_edit.setText("Default Text")
        line_edit.setPlaceholderText("Enter here...")
        # line_edit.setDisabled(True)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
