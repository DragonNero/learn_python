import sys, sqlite3
from functools import partial

from PyQt5 import QtCore, QtGui, QtWidgets

database = sqlite3.connect('Travel_list.db')
cur = database.cursor()


class Ui_MainWindow(object):
    def __init__(self):
        self.selectedTable = 'Categories'

    def setupUi(self, MainWindow):

        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)

        self.layout = QtWidgets.QGridLayout()
        self.selectBox = QtWidgets.QComboBox()
        self.selectBox.addItems(["Categories", "Items"])
        self.selectBox.currentTextChanged.connect(self.selectionChange)
        self.layout.addWidget(self.selectBox, 0, 0)

        self.addButton = QtWidgets.QPushButton(self.centralWidget)
        self.layout.addWidget(self.addButton, 0, 1)

        self.labelBox = QtWidgets.QLabel('<h1>Categories</h1>')
        self.layout.addWidget(self.labelBox, 1, 0)
        self.layout.addWidget(self.displayCategoryTable(), 2, 0, 1, 2)

        self.centralWidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Manage items and categories")
        self.addButton.setText("Add")

    def LoadDialogWindow(self):
        DialogWindow = QtWidgets.QMainWindow()
        ui = Ui_DialogWindow()
        ui.setupUi(DialogWindow)
        DialogWindow.show()

    def displayCategoryTable(self):
        cur.execute('SELECT id, title FROM category')
        categories = cur.fetchall()

        categoriesTable = QtWidgets.QTableWidget()
        categoriesTable.setRowCount(len(categories)+1)
        categoriesTable.setColumnCount(2)
        categoriesTable.setItem(0,0,QtWidgets.QTableWidgetItem('Id'))
        categoriesTable.setItem(0,1,QtWidgets.QTableWidgetItem('Title'))

        numberOfRow = 1
        for category in categories:
            categoriesTable.setItem(numberOfRow,0,QtWidgets.QTableWidgetItem(str(category[0])))
            categoriesTable.setItem(numberOfRow,1,QtWidgets.QTableWidgetItem(category[1]))
            numberOfRow  = numberOfRow  + 1

        return categoriesTable

    def displayItemTable(self):
        cur.execute('SELECT i.id, c.title AS category, i.title AS item FROM item i LEFT JOIN category c ON c.id = i.category_id')
        items = cur.fetchall()

        itemsTable = QtWidgets.QTableWidget()
        itemsTable.setRowCount(len(items)+1)
        itemsTable.setColumnCount(3)
        itemsTable.setItem(0,0,QtWidgets.QTableWidgetItem('Id'))
        itemsTable.setItem(0,1,QtWidgets.QTableWidgetItem('Category'))
        itemsTable.setItem(0,2,QtWidgets.QTableWidgetItem('Title'))

        numberOfRow = 1
        for item in items:
            itemsTable.setItem(numberOfRow,0,QtWidgets.QTableWidgetItem(str(item[0])))
            itemsTable.setItem(numberOfRow,1,QtWidgets.QTableWidgetItem(item[1]))
            itemsTable.setItem(numberOfRow,2,QtWidgets.QTableWidgetItem(item[2]))
            numberOfRow  = numberOfRow  + 1

        return itemsTable

    def selectionChange(self, text):
        self.layout.itemAt(3).widget().deleteLater()
        self.selectedTable = text
        if text == "Categories":
            self.labelBox.setText('<h1>Categories</h1>')
            self.layout.addWidget(self.displayCategoryTable(), 2, 0, 1, 2)
        elif text == "Items":
            self.labelBox.setText('<h1>Items</h1>')
            self.layout.addWidget(self.displayItemTable(), 2, 0, 1, 2)
        else:
            print('Group is not defined')

class Ui_DialogWindow(object):
    def __init__(self, selectedTable):
        self.selectedTable = selectedTable

    def setupUi(self, DialogWindow):
        DialogWindow.setObjectName("DialogWindow")
        DialogWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(DialogWindow)
        self.layout = QtWidgets.QGridLayout()

        self.labelBox = QtWidgets.QLabel('<h1>Add '+ self.selectedTable+'</h1>')
        self.layout.addWidget(self.labelBox, 0, 0, 1, 2)

        self.cancelButton = QtWidgets.QPushButton(self.centralWidget)
        self.cancelButton.clicked.connect(partial(self.Cancel, DialogWindow))
        self.layout.addWidget(self.cancelButton, 3, 0)

        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.layout.addWidget(self.saveButton, 3, 1)

        self.centralWidget.setLayout(self.layout)
        DialogWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(DialogWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Add Window")
        self.cancelButton.setText("Cancel")
        self.saveButton.setText("Save")

    def Cancel (self, DialogWindow):
        DialogWindow.close()


class Controller:

    def __init__(self):
        pass

    def Show_MainWindow(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow()
        self.mainUi.setupUi(self.MainWindow)
        self.mainUi.addButton.clicked.connect(self.Show_DialogWindow)

        self.MainWindow.show()

    def Show_DialogWindow(self):

        self.DialogWindow = QtWidgets.QMainWindow()
        self.DialogUi = Ui_DialogWindow(self.mainUi.selectedTable)
        self.DialogUi.setupUi(self.DialogWindow)

        self.DialogWindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_MainWindow()
    sys.exit(app.exec_())
