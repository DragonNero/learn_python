from PyQt5 import QtCore, QtWidgets, QtGui
from functools import partial

class Ui_CheckListWindow(object):
    def __init__(self, database, controller):
        self.database = database
        self.controller = controller
        self.cur = self.database.cursor()

    def setupUi(self, MainWindow):

        #MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)

        self.layout = QtWidgets.QGridLayout()

        self.labelBox = QtWidgets.QLabel('<h1>Check list</h1>')
        self.layout.addWidget(self.labelBox, 0, 0, 1, 2)

        self.centralWidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Check list")
