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

        self.cur.execute('SELECT ci.id, i.title, ci.checked FROM checklist_item ci LEFT JOIN item i ON ci.item_id = i.id WHERE ci.checklist_id = (SELECT MAX (id) FROM checklist) ORDER BY i.category_id')
        checkListItems = self.cur.fetchall()
        rowCounter = 1
        for item in checkListItems:
            self.itemCheck = QtWidgets.QCheckBox(item[1])
            self.itemCheck.clicked.connect(partial(self.updateCheckListItem, item[0], self.itemCheck))
            self.layout.addWidget(self.itemCheck, rowCounter, 0)
            rowCounter = rowCounter + 1

        self.centralWidget.setLayout(self.layout)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle("Check list")

    def updateCheckListItem(self, checkListItemId, checkBox):
        print(checkListItemId, checkBox.isChecked())
