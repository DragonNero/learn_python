import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('Manage items and categories')
window.setGeometry(0, 0, 400, 80)
helloMsg = QLabel('<h1>Hello I am Dragon!</h1>', parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec_())
