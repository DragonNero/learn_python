from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def __init__(self, database):
        self.database = database
        self.selectedTable = 'Categories'
        self.cur = self.database.cursor()
        self.cur.execute('SELECT id, title FROM category ORDER BY title ASC')
        self.categories = self.cur.fetchall()

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


        categoriesTable = QtWidgets.QTableWidget()
        categoriesTable.setRowCount(len(self.categories)+1)
        categoriesTable.setColumnCount(2)
        categoriesTable.setItem(0,0,QtWidgets.QTableWidgetItem('Id'))
        categoriesTable.setItem(0,1,QtWidgets.QTableWidgetItem('Title'))

        numberOfRow = 1
        for category in self.categories:
            categoriesTable.setItem(numberOfRow,0,QtWidgets.QTableWidgetItem(str(category[0])))
            categoriesTable.setItem(numberOfRow,1,QtWidgets.QTableWidgetItem(category[1]))
            numberOfRow  = numberOfRow  + 1

        return categoriesTable

    def displayItemTable(self):
        self.cur.execute('SELECT i.id, c.title AS category, i.title AS item FROM item i LEFT JOIN category c ON c.id = i.category_id')
        items = self.cur.fetchall()

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
