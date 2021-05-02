# = - an assignment(is)    == - comparison
import sys, sqlite3
from PyQt5 import QtWidgets
from checklist.Controller import Controller

database = sqlite3.connect('Travel_list.db')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller(database)
    Controller.Show_MainWindow()
    #cur.close()
    sys.exit(app.exec_())
