import sys, sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

database = sqlite3.connect('Travel_list.db')
cur = database.cursor()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName('Manage items and categories')
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)

        self.layout = QtWidgets.QGridLayout()
        self.selectBox = QtWidgets.QComboBox()
        self.selectBox.addItems(["Categories", "Items"])
        self.selectBox.currentTextChanged.connect(self.selectionChange)
        self.layout.addWidget(self.selectBox, 0, 0)

        self.addButton = QtWidgets.QPushButton(self.centralWidget)
        self.addButton.setObjectName("Add")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addButton.setText(_translate("MainWindow", "LoadDialogWindow"))

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
        if text == "Categories":
            self.labelBox.setText('<h1>Categories</h1>')
            self.layout.addWidget(self.displayCategoryTable(), 2, 0, 1, 2)
        elif text == "Items":
            self.labelBox.setText('<h1>Items</h1>')
            self.layout.addWidget(self.displayItemTable(), 2, 0, 1, 2)
        else:
            print('Group is not defined')

class Ui_DialogWindow(object):

    def setupUi(self, DialogWindow):
        DialogWindow.setObjectName("DialogWindow")
        DialogWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(DialogWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 130, 191, 23))
        self.pushButton.setObjectName("pushButton")
        DialogWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(DialogWindow)
        QtCore.QMetaObject.connectSlotsByName(DialogWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DialogWindow", "DialogWindow"))
        self.pushButton.setText(_translate("DialogWindow", "Congratz !"))



class Controller:

    def __init__(self):
        pass

    def Show_MainWindow(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.ui.addButton.clicked.connect(self.Show_DialogWindow)

        self.MainWindow.show()

    def Show_DialogWindow(self):

        self.DialogWindow = QtWidgets.QMainWindow()
        self.ui = Ui_DialogWindow()
        self.ui.setupUi(self.DialogWindow)
        self.ui.pushButton.clicked.connect(self.Print)

        self.DialogWindow.show()

    def Print(self):
        print('After 99 hours of trying out everything')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.Show_MainWindow()
    sys.exit(app.exec_())
