from functools import partial
from PyQt5 import QtCore, QtWidgets

class Ui_DialogWindow(object):
    def __init__(self, selectedTable, database):
        self.selectedTable = selectedTable
        self.database = database
        self.cur = self.database.cursor()
        self.cur.execute('SELECT id, title FROM category ORDER BY title ASC')
        self.categories = self.cur.fetchall()

    def setupUi(self, DialogWindow):
        DialogWindow.setObjectName("DialogWindow")
        DialogWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(DialogWindow)
        self.layout = QtWidgets.QGridLayout()

        self.labelBox = QtWidgets.QLabel('<h1>Add '+ self.selectedTable+'</h1>')
        self.layout.addWidget(self.labelBox, 0, 0, 1, 2)

        self.inputTitleLabel = QtWidgets.QLabel('Title')
        self.layout.addWidget(self.inputTitleLabel, 1, 0)
        self.inputTitle = QtWidgets.QLineEdit()
        self.layout.addWidget(self.inputTitle, 1, 1)

        if self.selectedTable == 'Items':
            self.selectCategoryLabel = QtWidgets.QLabel('Category')
            self.layout.addWidget(self.selectCategoryLabel, 2, 0)
            self.selectCategory = QtWidgets.QComboBox()
            for category in self.categories:
                self.selectCategory.addItem(category[1])
            self.layout.addWidget(self.selectCategory, 2, 1)

        self.cancelButton = QtWidgets.QPushButton(self.centralWidget)
        self.cancelButton.clicked.connect(partial(self.Cancel, DialogWindow))
        self.layout.addWidget(self.cancelButton, 3, 0)

        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.saveButton.clicked.connect(partial(self.Save, DialogWindow))
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

    def Save (self, DialogWindow):
        if self.selectedTable != "Categories" and self.selectedTable != "Items":
            print('Group is not defined')
            return

        titleValue = self.inputTitle.text().strip()
        if titleValue == '':
            print('Add value')
            return

        if self.selectedTable == "Categories":
            self.cur.execute('INSERT INTO category (title) VALUES (?)',(titleValue,))
            self.database.commit()
        elif self.selectedTable == "Items":
            selectedCategory = self.selectCategory.currentText()
            self.cur.execute('INSERT INTO item (category_id, title) VALUES ((SELECT id FROM category WHERE title = ? LIMIT 1),?)',(selectedCategory, titleValue))
            self.database.commit()
            #To do added to the table of the main window
        DialogWindow.close()
