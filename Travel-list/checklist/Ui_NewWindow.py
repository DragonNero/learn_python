from PyQt5 import QtCore, QtWidgets, QtGui
from functools import partial

class Ui_NewWindow(object):
    def __init__(self, database, controller):
        self.database = database
        self.controller = controller
        self.cur = self.database.cursor()
        self.selectedCategories = []

    def setupUi(self, NewWindow):

        #MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(NewWindow)

        self.layout = QtWidgets.QGridLayout()
        self.labelBox = QtWidgets.QLabel('<h1>Create a new check list</h1>')
        self.layout.addWidget(self.labelBox, 0, 0, 1, 4)

        self.sublabelBox = QtWidgets.QLabel('Select what you will do:')
        self.layout.addWidget(self.sublabelBox, 1, 0, 1, 4)

        rowCounter = 2
        self.cur.execute('SELECT id, title FROM category ORDER BY title ASC')
        categories = self.cur.fetchall()
        for index, category in enumerate(categories):
            colCounter = index % 4
            self.categoryCheck = QtWidgets.QCheckBox(category[1])
            self.categoryCheck.clicked.connect(partial(self.updateSelectedCategories, category[0], self.categoryCheck))
            self.layout.addWidget(self.categoryCheck, rowCounter, colCounter)
            if colCounter == 3:
                rowCounter = rowCounter + 1

        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.layout.addWidget(self.startButton, rowCounter+1, 4)
        self.startButton.clicked.connect(partial(self.start, NewWindow))

        self.centralWidget.setLayout(self.layout)
        NewWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(NewWindow)
        QtCore.QMetaObject.connectSlotsByName(NewWindow)


    def retranslateUi(self, NewWindow):
        _translate = QtCore.QCoreApplication.translate
        NewWindow.setWindowTitle("Create new checklist")
        self.startButton.setText("Start")

    def start(self, NewWindow):
        if not self.selectedCategories:
            print('List is empty')
            return

        self.cur.execute('SELECT id FROM item WHERE category_id IN ({catIds})'.format(catIds = ','.join(['?']*len(self.selectedCategories))), self.selectedCategories)
        items = self.cur.fetchall()
        self.cur.execute('INSERT INTO checklist (title) VALUES (?)', ('myCheckList',))
        checkListId = self.cur.lastrowid

        for categoryId in self.selectedCategories:
            self.cur.execute('INSERT INTO checklist_category (checklist_id, category_id) VALUES (?, ?)', (checkListId, categoryId))

        for itemId in items:
            self.cur.execute('INSERT INTO checklist_item (checklist_id, item_id) VALUES (?, ?)', (checkListId, itemId[0]))

        self.database.commit()
        self.controller.Show_CheckListWindow()
        NewWindow.close()

    def updateSelectedCategories(self, categoryId, checkBox):
        if checkBox.isChecked() == True:
            self.selectedCategories.append(categoryId)
        else:
            self.selectedCategories.remove(categoryId)
