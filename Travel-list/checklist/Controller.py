from PyQt5 import QtWidgets
from .Ui_NewWindow import Ui_NewWindow
from .Ui_MainWindow import Ui_MainWindow
from .Ui_CheckListWindow import Ui_CheckListWindow

class Controller:

    def __init__(self, database):
        self.database = database
        pass

    def Show_MainWindow(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow(self.database, self)
        self.mainUi.setupUi(self.MainWindow)
        self.mainUi.newButton.clicked.connect(self.Show_NewWindow)
        self.mainUi.openButton.clicked.connect(self.Show_CheckListWindow)

        self.MainWindow.show()

    def Show_NewWindow(self):
        self.NewWindow = QtWidgets.QMainWindow()
        self.NewUi = Ui_NewWindow(self.database, self)
        self.NewUi.setupUi(self.NewWindow)

        self.NewWindow.show()

    def Show_CheckListWindow(self):
        self.CheckListWindow = QtWidgets.QMainWindow()
        self.CheckListUi = Ui_CheckListWindow(self.database, self)
        self.CheckListUi.setupUi(self.CheckListWindow)

        self.CheckListWindow.show()
