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
    <h1>Categories</h1>
    <style>
    table {
     border-collapse: collapse;
     width: 100%;
    }
    table td, table th {
     border: 1px solid #ddd;
     padding: 8px;
    }
    table tr:hover {background-color: #ddd;}
    table th {
     padding-top: 12px;
     padding-bottom: 12px;
     text-align: left;
     background-color: #96999F;
     color: white;
    }
    </style>
    <table>
        <thead>
            <tr>
                <th>Id</th>
                <th>Title</th>
            </tr>
        </thead>
        <tbody>
"""
    for category in categories:
        categoriesTable += "<tr><td>"+str(category[0])+"</td><td>"+category[1]+"</td></tr>"

    categoriesTable += """
        </tbody>
    </table>
"""
    return categoriesTable




def displayItemTable():
    cur.execute('SELECT i.id, c.title AS category, i.title AS item FROM item i LEFT JOIN category c ON c.id = i.category_id')
    items = cur.fetchall()
    itemsTable = """
    <h1>Items</h1>
    <style>
    table {
     border-collapse: collapse;
     width: 100%;
    }
    table td, table th {
     border: 1px solid #ddd;
     padding: 8px;
    }
    table tr:hover {background-color: #ddd;}
    table th {
     padding-top: 12px;
     padding-bottom: 12px;
     text-align: left;
     background-color: #96999F;
     color: white;
    }
    </style>
    <table>
        <thead>
            <tr>
                <th>Id</th>
                <th>Category</th>
                <th>Title</th>
            </tr>
        </thead>
        <tbody>
"""
    for item in items:
        itemsTable += "<tr><td>"+str(item[0])+"</td><td>"+item[1]+"</td><td>"+item[2]+"</td></tr>"

    itemsTable += """
        </tbody>
    </table>
"""
    return itemsTable


def selectionchange(text):
    if text == "Categories":
        labelBox.setText(displayCategoryTable())
    elif text == "Items":
        labelBox.setText(displayItemTable())
    else:
        print('Group is not defined')

window = QWidget()
window.setWindowTitle('Manage items and categories')
layout = QGridLayout()
selectBox = QComboBox()
selectBox.addItems(["Categories", "Items"])
selectBox.currentTextChanged.connect(selectionchange)
layout.addWidget(selectBox, 0, 0)
layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
labelBox = QLabel(displayCategoryTable())
layout.addWidget(labelBox, 1, 0, 1, 2)

window.setLayout(layout)
window.show()

sys.exit(app.exec_())
