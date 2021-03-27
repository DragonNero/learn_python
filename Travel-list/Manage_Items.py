import sys
import sqlite3

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

database = sqlite3.connect('Travel_list.db')
cur = database.cursor()

app = QApplication(sys.argv)

def displayCategoryTable():
    cur.execute('SELECT id, title FROM category')
    categories = cur.fetchall()
    categoriesTable = """
    <table>
        <thead>
            <tr>
                <th>Id</th>
                <th>Title</th>
            </tr>
        </thead>
        <tbody>
"""
    categoriesTable += """
        </tbody>
        </table>
"""
    return categoriesTable




def displayItemTable():
    return '<h1>Item</h1>'

def selectionchange(text):
    if text == "Categories":
        labelBox.setText(displayCategoryTable())
    elif text == "Items":
        labelBox.setText(displayItemTable())
    else:
        print('Group is not defined')

window = QWidget()
window.setWindowTitle('Manage items and categories')
#window.setGeometry(0, 0, 400, 80)
layout = QGridLayout()
selectBox = QComboBox()
selectBox.addItems(["Categories", "Items"])
selectBox.currentTextChanged.connect(selectionchange)
layout.addWidget(selectBox, 0, 0)
labelBox = QLabel(displayCategoryTable())
layout.addWidget(labelBox, 1, 0)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
