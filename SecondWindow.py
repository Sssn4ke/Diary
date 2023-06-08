import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow, today_date, css_styles):
        '''Строит дерево виджетов и элементы интерфейса.'''
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(400, 600)
        self.css_styles = css_styles
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(260, 60, 70, 40))
        self.timeEdit.setObjectName("timeEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 60, 160, 130))
        self.textEdit.setObjectName("textEdit")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 210, 300, 260))
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.button_for_adding = QtWidgets.QPushButton(self.centralwidget)
        self.button_for_adding.setGeometry(QtCore.QRect(250, 120, 90, 70))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.button_for_adding.setFont(font)
        self.button_for_adding.setStyleSheet("background-color: rgb(159, 165, 160);\n"
                                             "border-radius: 20px;")
        self.button_for_adding.setObjectName("button_for_adding")
        self.button_for_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_for_save.setGeometry(QtCore.QRect(60, 520, 110, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.button_for_save.setFont(font)
        self.button_for_save.setStyleSheet("background-color: rgb(159, 165, 160);\n"
                                           "border-radius: 20px;")
        self.button_for_save.setObjectName("button_for_save")
        self.button_for_removing = QtWidgets.QPushButton(self.centralwidget)
        self.button_for_removing.setGeometry(QtCore.QRect(230, 520, 110, 50))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        self.button_for_removing.setFont(font)
        self.button_for_removing.setStyleSheet("background-color: rgb(159, 165, 160);\n"
                                               "border-radius: 20px;")
        self.button_for_removing.setObjectName("button_for_removing")
        self.Backgrounddd = QtWidgets.QLabel(self.centralwidget)
        self.Backgrounddd.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.Backgrounddd.setText("")
        self.Backgrounddd.setPixmap(QtGui.QPixmap("D:/Загрузки/background_of_diary.jpg"))
        self.Backgrounddd.setObjectName("Backgrounddd")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(50, 470, 300, 30))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.Backgrounddd.raise_()
        self.timeEdit.raise_()
        self.textEdit.raise_()
        self.listWidget.raise_()
        self.button_for_adding.raise_()
        self.button_for_save.raise_()
        self.button_for_removing.raise_()
        self.progressBar.raise_()
        SecondWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

        self.add_functions(today_date)

    def retranslateUi(self, SecondWindow):
        '''Устанавливает текст и заголовки виджетов.'''
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "Task Manager"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.button_for_adding.setText(_translate("SecondWindow", "Add"))
        self.button_for_save.setText(_translate("SecondWindow", "Save"))
        self.button_for_removing.setText(_translate("SecondWindow", "Delete"))

    def add_functions(self, today_date):
        '''Добавляет все необходимые функции для корректной работы приложения.'''
        self.update_window(today_date)
        self.update_styles()

        self.button_for_adding.clicked.connect(lambda: self.add_task(self.textEdit.toPlainText(), today_date))
        self.button_for_save.clicked.connect(lambda: self.save_changes(today_date))
        self.button_for_removing.clicked.connect(lambda: self.remove_task(today_date))

    def update_window(self, date):
        '''Обновляет задачи и прогресс в окне.'''
        self.update_tasks(date)
        self.update_progress_bar(date)

    def add_task(self, new_task, date):
        '''Добавляет задачу в базу данных.'''
        new_task = new_task.replace('\n', '')
        if new_task != "":
            db = sqlite3.connect("data.db")
            cursor = db.cursor()

            cursor.execute("CREATE TABLE IF NOT EXISTS Tasks (id INTEGER Primary key, task TEXT NOT NULL, completed INTEGER, date TEXT)")
            db.commit()

            task_time_qt = self.timeEdit.time()
            task_time = task_time_qt.toString("hh:mm")

            if task_time != "00:00":
                new_task = new_task + ' - ' + task_time

            cursor.execute("SELECT COALESCE(MAX(id)+1, 1) from Tasks")
            ID = cursor.fetchone()[0]

            query = "INSERT INTO Tasks(id, task, completed, date) VALUES (?,?,?,?)"
            row = (ID, new_task, 0, date,)

            cursor.execute(query, row)
            db.commit()

            self.update_window(date)
            self.textEdit.clear()

    def remove_task(self, date):
        '''Удаляет задачу'''
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        removing_item = self.listWidget.currentItem()
        removing_task = removing_item.text()
        removing_completed = 1 if removing_item.checkState() == QtCore.Qt.Checked else 0

        query1 = "SELECT id FROM Tasks WHERE task = ? and completed = ? and date = ?"
        row1 = (removing_task, removing_completed, date, )
        result_id = cursor.execute(query1, row1).fetchone()

        cursor.execute("DELETE from Tasks WHERE id = ?", (result_id[0], ))
        db.commit()

        self.update_window(date)

    def update_tasks(self, date):
        '''Обновляет список с задачами из базы данных.'''
        self.listWidget.clear()

        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        cursor.execute("CREATE TABLE IF NOT EXISTS Tasks (id INTEGER Primary key, task TEXT NOT NULL, completed INTEGER, date TEXT)")
        db.commit()

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

        messageBox = QMessageBox()
        messageBox.setStyleSheet("min-width: 150px;");
        messageBox.setText("Changes saved!")
        messageBox.setWindowTitle("Notification")
        messageBox.setStandardButtons(QMessageBox.Ok)
        messageBox.exec()

        self.update_window(date)

    def update_progress_bar(self, date):
        '''Обновляет шкалу прогресса.'''
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        query1 = "SELECT count() FROM Tasks WHERE date = ?"
        row = (date, )
        num_of_tasks = cursor.execute(query1, row).fetchall()[0][0]

        query2 = "SELECT count() FROM Tasks WHERE completed = 1 and date = ?"
        num_of_completed_tasks = cursor.execute(query2, row).fetchall()[0][0]

        percentage = num_of_completed_tasks / num_of_tasks * 100 if num_of_tasks != 0 else 0
        self.progressBar.setValue(percentage)

    def update_styles(self):
        '''Устанавливает цвет кнопок.'''
        if self.css_styles[2] == "Default":
            self.button_for_save.setStyleSheet("background-color: rgb(159, 165, 160);\n"
                                               "border-radius: 20px;")
            self.button_for_adding.setStyleSheet("background-color: rgb(159, 165, 160);\n"
                                                 "border-radius: 20px;")
            self.button_for_removing.setStyleSheet("background-color: rgb(159, 165, 160);\n"
                                                   "border-radius: 20px;")
        if self.css_styles[2] == "Green":
            self.button_for_save.setStyleSheet("background-color: rgb(0, 208, 0);\n"
                                               "border-radius: 20px;")
            self.button_for_adding.setStyleSheet("background-color: rgb(0, 208, 0);\n"
                                                 "border-radius: 20px;")
            self.button_for_removing.setStyleSheet("background-color: rgb(0, 208, 0);\n"
                                                   "border-radius: 20px;")
        if self.css_styles[2] == "Orange":
            self.button_for_save.setStyleSheet("background-color: rgb(255, 159, 3);\n"
                                               "border-radius: 20px;")
            self.button_for_adding.setStyleSheet("background-color: rgb(255, 159, 3);\n"
                                                 "border-radius: 20px;")
            self.button_for_removing.setStyleSheet("background-color: rgb(255, 159, 3);\n"
                                                   "border-radius: 20px;")
        if self.css_styles[2] == "Blue":
            self.button_for_save.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                               "border-radius: 20px;")
            self.button_for_adding.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                                 "border-radius: 20px;")
            self.button_for_removing.setStyleSheet("background-color: rgb(85, 170, 255);\n"
                                                   "border-radius: 20px;")
        if self.css_styles[2] == "Black":
            self.button_for_save.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "border-radius: 20px;")
            self.button_for_adding.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border-radius: 20px;")
            self.button_for_removing.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                   "border-radius: 20px;")
        if self.css_styles[2] == "White":
            self.button_for_save.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                               "border-radius: 20px;")
            self.button_for_adding.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                 "border-radius: 20px;")
            self.button_for_removing.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                                   "border-radius: 20px;")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QWidget.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
