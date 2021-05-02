from PyQt5 import QtCore, QtWidgets, QtGui
from functools import partial

class Ui_MainWindow(object):
    def __init__(self, database, controller):
        self.database = database
        self.controller = controller
        self.cur = self.database.cursor()

    def setupUi(self, MainWindow):

        #MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)

        self.layout = QtWidgets.QGridLayout()

        self.labelBox = QtWidgets.QLabel('<h1>Travel check list</h1>')
        self.layout.addWidget(self.labelBox, 0, 0, 1, 2)

        self.newButton = QtWidgets.QPushButton(self.centralWidget)
        self.layout.addWidget(self.newButton, 1, 0)

        self.openButton = QtWidgets.QPushButton(self.centralWidget)
        self.layout.addWidget(self.openButton, 1, 1)

        self.centralWidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Travel check list")
        self.newButton.setText("Create new checklist")
        self.openButton.setText("Open an existing checklist")
