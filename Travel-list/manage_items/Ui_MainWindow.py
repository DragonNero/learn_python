from PyQt5 import QtCore, QtWidgets, QtGui
from functools import partial

class Ui_MainWindow(object):
    def __init__(self, database):
        self.database = database
        self.selectedTable = 'Categories'
        self.cur = self.database.cursor()

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
        self.cur.execute('SELECT id, title FROM category ORDER BY title ASC')
        self.categories = self.cur.fetchall()

        self.mainTable = QtWidgets.QTableWidget()
        self.mainTable.setRowCount(len(self.categories)+1)
        self.mainTable.setColumnCount(3)
        self.mainTable.setItem(0,0,QtWidgets.QTableWidgetItem('Id'))
        self.mainTable.setItem(0,1,QtWidgets.QTableWidgetItem('Title'))
        self.mainTable.setItem(0,2,QtWidgets.QTableWidgetItem(''))

        numberOfRow = 1
        for category in self.categories:
            self.mainTable.setItem(numberOfRow,0,QtWidgets.QTableWidgetItem(str(category[0])))
            self.mainTable.setItem(numberOfRow,1,QtWidgets.QTableWidgetItem(category[1]))
            buttonDelete = QtWidgets.QPushButton()
            buttonDelete.setIcon(QtGui.QIcon('manage_items/trash.svg'))
            buttonDelete.clicked.connect(partial(self.Delete, category[0], numberOfRow))
            self.mainTable.setCellWidget(numberOfRow,2,buttonDelete)
            numberOfRow  = numberOfRow  + 1


        return self.mainTable

    def displayItemTable(self):
        self.cur.execute('SELECT i.id, c.title AS category, i.title AS item FROM item i LEFT JOIN category c ON c.id = i.category_id')
        items = self.cur.fetchall()

        self.mainTable = QtWidgets.QTableWidget()
        self.mainTable.setRowCount(len(items)+1)
        self.mainTable.setColumnCount(4)
        self.mainTable.setItem(0,0,QtWidgets.QTableWidgetItem('Id'))
        self.mainTable.setItem(0,1,QtWidgets.QTableWidgetItem('Category'))
        self.mainTable.setItem(0,2,QtWidgets.QTableWidgetItem('Title'))
        self.mainTable.setItem(0,3,QtWidgets.QTableWidgetItem(''))

        numberOfRow = 1
        for item in items:
            self.mainTable.setItem(numberOfRow,0,QtWidgets.QTableWidgetItem(str(item[0])))
            self.mainTable.setItem(numberOfRow,1,QtWidgets.QTableWidgetItem(item[1]))
            self.mainTable.setItem(numberOfRow,2,QtWidgets.QTableWidgetItem(item[2]))
            buttonDelete = QtWidgets.QPushButton()
            buttonDelete.setIcon(QtGui.QIcon('manage_items/trash.svg'))
            buttonDelete.clicked.connect(partial(self.Delete, item[0], numberOfRow))
            self.mainTable.setCellWidget(numberOfRow,3,buttonDelete)
            numberOfRow  = numberOfRow  + 1

        return self.mainTable

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

    def Delete(self, id, numberOfRow):
        if self.selectedTable == "Categories":
            # TODO delete the correct item when we delete multiple rows
            self.cur.execute('DELETE FROM item WHERE category_id = ?',(id,))
            self.cur.execute('DELETE FROM category WHERE id = ?',(id,))
            self.database.commit()
            self.mainTable.removeRow(numberOfRow)
        elif self.selectedTable == "Items":
            self.cur.execute('DELETE FROM item WHERE id = ?',(id,))
            self.database.commit()
            self.mainTable.removeRow(numberOfRow)
        else:
            print('Group is not defined')
