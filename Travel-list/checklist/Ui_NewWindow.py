from PyQt5 import QtCore, QtWidgets, QtGui
from functools import partial

class Ui_NewWindow(object):
    def __init__(self, database, controller):
        self.database = database
        self.controller = controller
        self.cur = self.database.cursor()

    def setupUi(self, NewWindow):

        #MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(NewWindow)

        self.layout = QtWidgets.QGridLayout()
        #TODO fill the interface
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
            self.layout.addWidget(self.categoryCheck, rowCounter, colCounter)
            if colCounter == 3:
                rowCounter = rowCounter + 1

        self.startButton = QtWidgets.QPushButton(self.centralWidget)
        self.layout.addWidget(self.startButton, rowCounter+1, 4)

        self.centralWidget.setLayout(self.layout)
        NewWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(NewWindow)
        QtCore.QMetaObject.connectSlotsByName(NewWindow)


    def retranslateUi(self, NewWindow):
        _translate = QtCore.QCoreApplication.translate
        NewWindow.setWindowTitle("Create new checklist")
        self.startButton.setText("Start")
