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
        self.labelBox = QtWidgets.QLabel('<h1>Travel check list</h1>')
        self.layout.addWidget(self.labelBox, 0, 0, 1, 2)

        self.newButton = QtWidgets.QPushButton(self.centralWidget)
        self.layout.addWidget(self.newButton, 1, 0)

        self.openButton = QtWidgets.QPushButton(self.centralWidget)
        self.layout.addWidget(self.openButton, 1, 1)

        self.centralWidget.setLayout(self.layout)
        NewWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(NewWindow)
        QtCore.QMetaObject.connectSlotsByName(NewWindow)


    def retranslateUi(self, NewWindow):
        _translate = QtCore.QCoreApplication.translate
        NewWindow.setWindowTitle("Create new checklist")
        self.newButton.setText("Create new checklist")
        self.openButton.setText("Open an existing checklist")
