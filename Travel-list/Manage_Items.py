import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

def selectionchange(text):
    labelBox.setText(text)
    print(text)

window = QWidget()
window.setWindowTitle('Manage items and categories')
#window.setGeometry(0, 0, 400, 80)
layout = QGridLayout()
selectBox = QComboBox()
selectBox.addItems(["Categories", "Items"])
selectBox.currentTextChanged.connect(selectionchange)
layout.addWidget(selectBox, 0, 0)
labelBox = QLabel('<h1>Hello I am Dragon!</h1>')
layout.addWidget(labelBox, 1, 0)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
