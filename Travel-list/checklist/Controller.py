from PyQt5 import QtWidgets
from .Ui_NewWindow import Ui_NewWindow
from .Ui_MainWindow import Ui_MainWindow

class Controller:

    def __init__(self, database):
        self.database = database
        pass

    def Show_MainWindow(self):

        self.MainWindow = QtWidgets.QMainWindow()
        self.mainUi = Ui_MainWindow(self.database, self)
        self.mainUi.setupUi(self.MainWindow)
        self.mainUi.newButton.clicked.connect(self.Show_NewWindow)

        self.MainWindow.show()

    def Show_NewWindow(self):

        self.NewWindow = QtWidgets.QMainWindow()
        self.NewUi = Ui_NewWindow(self.database, self)
        self.NewUi.setupUi(self.NewWindow)

        self.NewWindow.show()
