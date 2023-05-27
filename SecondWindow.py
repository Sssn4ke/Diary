import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow, today_date):
        '''Строит дерево виджетов и элементы интерфейса.'''
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(400, 600)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 210, 300, 370))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(120, 20, 160, 40))
        self.timeEdit.setObjectName("timeEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 80, 160, 50))
        self.textEdit.setObjectName("textEdit")
        self.button_for_adding = QtWidgets.QPushButton(self.centralwidget)
        self.button_for_adding.setGeometry(QtCore.QRect(140, 146, 120, 40))
        self.button_for_adding.setObjectName("button_for_adding")
        self.Backgrounddd = QtWidgets.QLabel(self.centralwidget)
        self.Backgrounddd.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.Backgrounddd.setText("")
        self.Backgrounddd.setPixmap(QtGui.QPixmap("../../../Downloads/background_of_diary.jpg"))
        self.Backgrounddd.setObjectName("Backgrounddd")
        self.Backgrounddd.raise_()
        self.listWidget.raise_()
        self.timeEdit.raise_()
        self.textEdit.raise_()
        self.button_for_adding.raise_()
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

        self.add_functions(today_date)

    def retranslateUi(self, SecondWindow):
        '''Устанавливает текст и заголовки виджетов.'''
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "Timetable"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.button_for_adding.setText(_translate("SecondWindow", "Add"))

    def add_functions(self, today_date):
        '''Добавляет все необходимые функции для корректной работы приложения.'''
        self.update_tasks(today_date)

        self.button_for_adding.clicked.connect(lambda: self.add_task(self.textEdit.toPlainText(), today_date))

    def add_task(self, new_task, date):
        '''Добавляет задачу в базу данных.'''
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        task_time_qt = self.timeEdit.time()
        task_time = task_time_qt.toString("hh:mm")

        if task_time != "00:00":
            new_task = new_task + ' - ' + task_time

        query = "INSERT INTO Tasks(task, completed, date) VALUES (?,?,?)"
        row = (new_task, 0, date,)

        cursor.execute(query,row)
        db.commit()

        self.save_changes(date)
        self.update_tasks(date)

    def update_tasks(self, date):
        '''Обновляет список с задачами из базы данных.'''
        self.listWidget.clear()

        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        query = "SELECT task, completed FROM Tasks Where date = ?"
        row = (date, )
        results = cursor.execute(query, row).fetchall()

        for result in results:
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEditable)
            if result[1] == 1:
                item.setCheckState(QtCore.Qt.Checked)
            elif result[1] == 0:
                item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)

    def save_changes(self, date):
        '''Сохраняет изменения в базу данных.'''
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE Tasks SET completed = 1 WHERE task = ? and date = ?"
            else:
                query = "UPDATE Tasks SET completed = 0 WHERE task = ? and date = ?"
            row = (task, date,)
            cursor.execute(query, row)

        db.commit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QWidget()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
