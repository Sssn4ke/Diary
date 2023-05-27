from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
class Ui_MainWindow(object):
    def add_label(self, MainWindow):
        print("add")
    def add_logics(self, MainWindow):
        self.p2.clicked.connect(self.add_label)
