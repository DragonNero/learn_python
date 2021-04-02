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

    categoriesTable = QTableWidget()
    categoriesTable.setRowCount(len(categories)+1)
    categoriesTable.setColumnCount(2)
    categoriesTable.setItem(0,0,QTableWidgetItem('Id'))
    categoriesTable.setItem(0,1,QTableWidgetItem('Title'))

    numberOfRow = 1
    for category in categories:
        categoriesTable.setItem(numberOfRow,0,QTableWidgetItem(str(category[0])))
        categoriesTable.setItem(numberOfRow,1,QTableWidgetItem(category[1]))
        numberOfRow  = numberOfRow  + 1

    return categoriesTable

def displayItemTable():
    cur.execute('SELECT i.id, c.title AS category, i.title AS item FROM item i LEFT JOIN category c ON c.id = i.category_id')
    items = cur.fetchall()

    itemsTable = QTableWidget()
    itemsTable.setRowCount(len(items)+1)
    itemsTable.setColumnCount(3)
    itemsTable.setItem(0,0,QTableWidgetItem('Id'))
    itemsTable.setItem(0,1,QTableWidgetItem('Category'))
    itemsTable.setItem(0,2,QTableWidgetItem('Title'))

    numberOfRow = 1
    for item in items:
        itemsTable.setItem(numberOfRow,0,QTableWidgetItem(str(item[0])))
        itemsTable.setItem(numberOfRow,1,QTableWidgetItem(item[1]))
        itemsTable.setItem(numberOfRow,2,QTableWidgetItem(item[2]))
        numberOfRow  = numberOfRow  + 1

    return itemsTable

def selectionChange(text):
    layout.itemAt(3).widget().deleteLater()
    if text == "Categories":
        labelBox.setText('<h1>Categories</h1>')
        layout.addWidget(displayCategoryTable(), 2, 0, 1, 2)
    elif text == "Items":
        labelBox.setText('<h1>Items</h1>')
        layout.addWidget(displayItemTable(), 2, 0, 1, 2)
    else:
        print('Group is not defined')

def addWindow():
    addWindow = QWidget()
    addWindow.setWindowTitle('Add items and categories')

    addLayout = QGridLayout()
    addLabelBox = QLabel('<h1>New</h1>')
    addLayout.addWidget(addLabelBox, 0, 0, 1, 2)
    addCancelButton = QPushButton('Cancel')
    addCancelButton.clicked.connect(closeWindow)
    addLayout.addWidget(addCancelButton, 2, 0)
    addSaveButton = QPushButton('Save')
    addLayout.addWidget(addSaveButton, 2, 1)
    addWindow.setLayout(addLayout)
    addWindow.show()

def closeWindow():
    addWindow.close()

window = QWidget()
window.setWindowTitle('Manage items and categories')
layout = QGridLayout()
selectBox = QComboBox()
selectBox.addItems(["Categories", "Items"])
selectBox.currentTextChanged.connect(selectionChange)
layout.addWidget(selectBox, 0, 0)

addButton = QPushButton('Add')
addButton.clicked.connect(addWindow)
layout.addWidget(addButton, 0, 1)

labelBox = QLabel('<h1>Categories</h1>')
layout.addWidget(labelBox, 1, 0)
layout.addWidget(displayCategoryTable(), 2, 0, 1, 2)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
