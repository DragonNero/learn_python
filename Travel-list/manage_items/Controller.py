from PyQt5 import QtWidgets
from .Ui_DialogWindow import Ui_DialogWindow
from .Ui_MainWindow import Ui_MainWindow

class Controller:

    def __init__(self, database):
        self.database = database
        pass

    def Show_MainWindow(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow(self.database, self)
        self.mainUi.setupUi(self.MainWindow)
        self.mainUi.addButton.clicked.connect(self.Show_DialogWindow)

        self.MainWindow.show()

    def Show_DialogWindow(self, editId):

        self.DialogWindow = QtWidgets.QMainWindow()
        self.DialogUi = Ui_DialogWindow(self.mainUi.selectedTable, self.database, self.mainUi, editId)
        self.DialogUi.setupUi(self.DialogWindow)

        self.DialogWindow.show()
