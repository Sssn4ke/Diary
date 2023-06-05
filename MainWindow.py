
from PyQt5.QtWidgets import QMenuBar, QMenu, QFileDialog, QPushButton
from datetime import datetime
from calendar import monthrange
from SecondWindow import Ui_SecondWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        '''Строит дерево виджетов и элементы интерфейса.'''
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Data_table = QtWidgets.QTableWidget(self.centralwidget)
        self.Data_table.setGeometry(QtCore.QRect(40, 170, 702, 212))
        self.Data_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Data_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.Data_table.setRowCount(7)
        self.Data_table.setColumnCount(7)
        self.Data_table.setObjectName("Data_table")
        self.Data_table.horizontalHeader().setVisible(False)
        self.Data_table.horizontalHeader().setDefaultSectionSize(100)
        self.Data_table.horizontalHeader().setMinimumSectionSize(39)
        self.Data_table.verticalHeader().setVisible(False)
        self.Data_table.verticalHeader().setDefaultSectionSize(30)
        self.Data_table.verticalHeader().setMinimumSectionSize(23)
        self.Month_year = QtWidgets.QLabel(self.centralwidget)
        self.Month_year.setGeometry(QtCore.QRect(290, 120, 220, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Month_year.setFont(font)
        self.Month_year.setAlignment(QtCore.Qt.AlignCenter)
        self.Month_year.setObjectName("Month_year")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Загрузки/background_of_diary.jpg"))
        self.label.setObjectName("label")
        self.p2 = QtWidgets.QPushButton(self.centralwidget)
        self.p2.setGeometry(QtCore.QRect(140, 200, 101, 31))
        self.p2.setObjectName("p2")
        self.p3 = QtWidgets.QPushButton(self.centralwidget)
        self.p3.setGeometry(QtCore.QRect(240, 200, 101, 31))
        self.p3.setObjectName("p3")
        self.p4 = QtWidgets.QPushButton(self.centralwidget)
        self.p4.setGeometry(QtCore.QRect(340, 200, 101, 31))
        self.p4.setObjectName("p4")
        self.p5 = QtWidgets.QPushButton(self.centralwidget)
        self.p5.setGeometry(QtCore.QRect(440, 200, 101, 31))
        self.p5.setObjectName("p5")
        self.p1 = QtWidgets.QPushButton(self.centralwidget)
        self.p1.setGeometry(QtCore.QRect(40, 200, 101, 31))
        self.p1.setObjectName("p1")
        self.p6 = QtWidgets.QPushButton(self.centralwidget)
        self.p6.setGeometry(QtCore.QRect(540, 200, 101, 31))
        self.p6.setObjectName("p6")
        self.p7 = QtWidgets.QPushButton(self.centralwidget)
        self.p7.setGeometry(QtCore.QRect(640, 200, 101, 31))
        self.p7.setObjectName("p7")
        self.p8 = QtWidgets.QPushButton(self.centralwidget)
        self.p8.setGeometry(QtCore.QRect(40, 230, 101, 31))
        self.p8.setObjectName("p8")
        self.p9 = QtWidgets.QPushButton(self.centralwidget)
        self.p9.setGeometry(QtCore.QRect(140, 230, 101, 31))
        self.p9.setObjectName("p9")
        self.p10 = QtWidgets.QPushButton(self.centralwidget)
        self.p10.setGeometry(QtCore.QRect(240, 230, 101, 31))
        self.p10.setObjectName("p10")
        self.p11 = QtWidgets.QPushButton(self.centralwidget)
        self.p11.setGeometry(QtCore.QRect(340, 230, 101, 31))
        self.p11.setObjectName("p11")
        self.p12 = QtWidgets.QPushButton(self.centralwidget)
        self.p12.setGeometry(QtCore.QRect(440, 230, 101, 31))
        self.p12.setObjectName("p12")
        self.p13 = QtWidgets.QPushButton(self.centralwidget)
        self.p13.setGeometry(QtCore.QRect(540, 230, 101, 31))
        self.p13.setObjectName("p13")
        self.p14 = QtWidgets.QPushButton(self.centralwidget)
        self.p14.setGeometry(QtCore.QRect(640, 230, 101, 31))
        self.p14.setObjectName("p14")
        self.p21 = QtWidgets.QPushButton(self.centralwidget)
        self.p21.setGeometry(QtCore.QRect(640, 260, 101, 31))
        self.p21.setObjectName("p21")
        self.p28 = QtWidgets.QPushButton(self.centralwidget)
        self.p28.setGeometry(QtCore.QRect(640, 290, 101, 31))
        self.p28.setObjectName("p28")
        self.p35 = QtWidgets.QPushButton(self.centralwidget)
        self.p35.setGeometry(QtCore.QRect(640, 320, 101, 31))
        self.p35.setObjectName("p35")
        self.p20 = QtWidgets.QPushButton(self.centralwidget)
        self.p20.setGeometry(QtCore.QRect(540, 260, 101, 31))
        self.p20.setObjectName("p20")
        self.p27 = QtWidgets.QPushButton(self.centralwidget)
        self.p27.setGeometry(QtCore.QRect(540, 290, 101, 31))
        self.p27.setObjectName("p27")
        self.p34 = QtWidgets.QPushButton(self.centralwidget)
        self.p34.setGeometry(QtCore.QRect(540, 320, 101, 31))
        self.p34.setObjectName("p34")
        self.p19 = QtWidgets.QPushButton(self.centralwidget)
        self.p19.setGeometry(QtCore.QRect(440, 260, 101, 31))
        self.p19.setObjectName("p19")
        self.p26 = QtWidgets.QPushButton(self.centralwidget)
        self.p26.setGeometry(QtCore.QRect(440, 290, 101, 31))
        self.p26.setObjectName("p26")
        self.p33 = QtWidgets.QPushButton(self.centralwidget)
        self.p33.setGeometry(QtCore.QRect(440, 320, 101, 31))
        self.p33.setObjectName("p33")
        self.p18 = QtWidgets.QPushButton(self.centralwidget)
        self.p18.setGeometry(QtCore.QRect(340, 260, 101, 31))
        self.p18.setObjectName("p18")
        self.p25 = QtWidgets.QPushButton(self.centralwidget)
        self.p25.setGeometry(QtCore.QRect(340, 290, 101, 31))
        self.p25.setObjectName("p25")
        self.p32 = QtWidgets.QPushButton(self.centralwidget)
        self.p32.setGeometry(QtCore.QRect(340, 320, 101, 31))
        self.p32.setObjectName("p32")
        self.p17 = QtWidgets.QPushButton(self.centralwidget)
        self.p17.setGeometry(QtCore.QRect(240, 260, 101, 31))
        self.p17.setObjectName("p17")
        self.p24 = QtWidgets.QPushButton(self.centralwidget)
        self.p24.setGeometry(QtCore.QRect(240, 290, 101, 31))
        self.p24.setObjectName("p24")
        self.p31 = QtWidgets.QPushButton(self.centralwidget)
        self.p31.setGeometry(QtCore.QRect(240, 320, 101, 31))
        self.p31.setObjectName("p31")
        self.p16 = QtWidgets.QPushButton(self.centralwidget)
        self.p16.setGeometry(QtCore.QRect(140, 260, 101, 31))
        self.p16.setObjectName("p16")
        self.p23 = QtWidgets.QPushButton(self.centralwidget)
        self.p23.setGeometry(QtCore.QRect(140, 290, 101, 31))
        self.p23.setObjectName("p23")
        self.p30 = QtWidgets.QPushButton(self.centralwidget)
        self.p30.setGeometry(QtCore.QRect(140, 320, 101, 31))
        self.p30.setObjectName("p30")
        self.p22 = QtWidgets.QPushButton(self.centralwidget)
        self.p22.setGeometry(QtCore.QRect(40, 290, 101, 31))
        self.p22.setObjectName("p22")
        self.p29 = QtWidgets.QPushButton(self.centralwidget)
        self.p29.setGeometry(QtCore.QRect(40, 320, 101, 31))
        self.p29.setObjectName("p29")
        self.p15 = QtWidgets.QPushButton(self.centralwidget)
        self.p15.setGeometry(QtCore.QRect(40, 260, 101, 31))
        self.p15.setObjectName("p15")
        self.p42 = QtWidgets.QPushButton(self.centralwidget)
        self.p42.setGeometry(QtCore.QRect(640, 350, 101, 31))
        self.p42.setObjectName("p42")
        self.p41 = QtWidgets.QPushButton(self.centralwidget)
        self.p41.setGeometry(QtCore.QRect(540, 350, 101, 31))
        self.p41.setObjectName("p41")
        self.p40 = QtWidgets.QPushButton(self.centralwidget)
        self.p40.setGeometry(QtCore.QRect(440, 350, 101, 31))
        self.p40.setObjectName("p40")
        self.p39 = QtWidgets.QPushButton(self.centralwidget)
        self.p39.setGeometry(QtCore.QRect(340, 350, 101, 31))
        self.p39.setObjectName("p39")
        self.p38 = QtWidgets.QPushButton(self.centralwidget)
        self.p38.setGeometry(QtCore.QRect(240, 350, 101, 31))
        self.p38.setObjectName("p38")
        self.p37 = QtWidgets.QPushButton(self.centralwidget)
        self.p37.setGeometry(QtCore.QRect(140, 350, 101, 31))
        self.p37.setObjectName("p37")
        self.p36 = QtWidgets.QPushButton(self.centralwidget)
        self.p36.setGeometry(QtCore.QRect(40, 350, 101, 31))
        self.p36.setObjectName("p36")
        self.Monday = QtWidgets.QLabel(self.centralwidget)
        self.Monday.setGeometry(QtCore.QRect(40, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Monday.setFont(font)
        self.Monday.setAlignment(QtCore.Qt.AlignCenter)
        self.Monday.setObjectName("Monday")
        self.Tuesday = QtWidgets.QLabel(self.centralwidget)
        self.Tuesday.setGeometry(QtCore.QRect(140, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Tuesday.setFont(font)
        self.Tuesday.setAlignment(QtCore.Qt.AlignCenter)
        self.Tuesday.setObjectName("Tuesday")
        self.Wednesday = QtWidgets.QLabel(self.centralwidget)
        self.Wednesday.setGeometry(QtCore.QRect(240, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Wednesday.setFont(font)
        self.Wednesday.setAlignment(QtCore.Qt.AlignCenter)
        self.Wednesday.setObjectName("Wednesday")
        self.Thursday = QtWidgets.QLabel(self.centralwidget)
        self.Thursday.setGeometry(QtCore.QRect(340, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Thursday.setFont(font)
        self.Thursday.setAlignment(QtCore.Qt.AlignCenter)
        self.Thursday.setObjectName("Thursday")
        self.Friday = QtWidgets.QLabel(self.centralwidget)
        self.Friday.setGeometry(QtCore.QRect(440, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Friday.setFont(font)
        self.Friday.setAlignment(QtCore.Qt.AlignCenter)
        self.Friday.setObjectName("Friday")
        self.Saturday = QtWidgets.QLabel(self.centralwidget)
        self.Saturday.setGeometry(QtCore.QRect(540, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Saturday.setFont(font)
        self.Saturday.setAlignment(QtCore.Qt.AlignCenter)
        self.Saturday.setObjectName("Saturday")
        self.Sunday = QtWidgets.QLabel(self.centralwidget)
        self.Sunday.setGeometry(QtCore.QRect(640, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Sunday.setFont(font)
        self.Sunday.setAlignment(QtCore.Qt.AlignCenter)
        self.Sunday.setObjectName("Sunday")
        self.Left_step = QtWidgets.QPushButton(self.centralwidget)
        self.Left_step.setGeometry(QtCore.QRect(160, 430, 160, 60))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Left_step.setFont(font)
        self.Left_step.setStyleSheet("background-color: rgb(159, 165, 160);\n"
                                     "border-radius: 20px;")
        self.Left_step.setObjectName("Left_step")
        self.Right_step = QtWidgets.QPushButton(self.centralwidget)
        self.Right_step.setGeometry(QtCore.QRect(480, 430, 160, 60))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Right_step.setFont(font)
        self.Right_step.setStyleSheet("background-color: rgb(159, 165, 160);\n"
                                      "border-radius: 20px;")
        self.Right_step.setObjectName("Right_step")
        self.label.raise_()
        self.Data_table.raise_()
        self.Month_year.raise_()
        self.p2.raise_()
        self.p3.raise_()
        self.p4.raise_()
        self.p5.raise_()
        self.p1.raise_()
        self.p6.raise_()
        self.p7.raise_()
        self.p8.raise_()
        self.p9.raise_()
        self.p10.raise_()
        self.p11.raise_()
        self.p12.raise_()
        self.p13.raise_()
        self.p14.raise_()
        self.p21.raise_()
        self.p28.raise_()
        self.p35.raise_()
        self.p20.raise_()
        self.p27.raise_()
        self.p34.raise_()
        self.p19.raise_()
        self.p26.raise_()
        self.p33.raise_()
        self.p18.raise_()
        self.p25.raise_()
        self.p32.raise_()
        self.p17.raise_()
        self.p24.raise_()
        self.p31.raise_()
        self.p16.raise_()
        self.p23.raise_()
        self.p30.raise_()
        self.p22.raise_()
        self.p29.raise_()
        self.p15.raise_()
        self.p42.raise_()
        self.p41.raise_()
        self.p40.raise_()
        self.p39.raise_()
        self.p38.raise_()
        self.p37.raise_()
        self.p36.raise_()
        self.Monday.raise_()
        self.Tuesday.raise_()
        self.Wednesday.raise_()
        self.Thursday.raise_()
        self.Friday.raise_()
        self.Saturday.raise_()
        self.Sunday.raise_()
        self.Left_step.raise_()
        self.Right_step.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuSettings")
        self.menuBackground = QtWidgets.QMenu(self.menuView)
        self.menuBackground.setObjectName("menuBackground")
        self.menuTypescreen = QtWidgets.QMenu(self.menuView)
        self.menuTypescreen.setObjectName("menuTypescreen")
        self.menuButton_Colour = QtWidgets.QMenu(self.menuView)
        self.menuButton_Colour.setObjectName("menuButton_Colour")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionJanuary = QtWidgets.QAction(MainWindow)
        self.actionJanuary.setObjectName("actionJanuary")
        self.actionFebruary = QtWidgets.QAction(MainWindow)
        self.actionFebruary.setObjectName("actionFebruary")
        self.actionMarch = QtWidgets.QAction(MainWindow)
        self.actionMarch.setObjectName("actionMarch")
        self.actionApril = QtWidgets.QAction(MainWindow)
        self.actionApril.setObjectName("actionApril")
        self.actionMay = QtWidgets.QAction(MainWindow)
        self.actionMay.setObjectName("actionMay")
        self.actionJune = QtWidgets.QAction(MainWindow)
        self.actionJune.setObjectName("actionJune")
        self.actionJuly = QtWidgets.QAction(MainWindow)
        self.actionJuly.setObjectName("actionJuly")
        self.actionAugust = QtWidgets.QAction(MainWindow)
        self.actionAugust.setObjectName("actionAugust")
        self.actionSeptember = QtWidgets.QAction(MainWindow)
        self.actionSeptember.setObjectName("actionSeptember")
        self.actionOctober = QtWidgets.QAction(MainWindow)
        self.actionOctober.setObjectName("actionOctober")
        self.actionNovember = QtWidgets.QAction(MainWindow)
        self.actionNovember.setObjectName("actionNovember")
        self.actionDecember = QtWidgets.QAction(MainWindow)
        self.actionDecember.setObjectName("actionDecember")
        self.actionDarkside = QtWidgets.QAction(MainWindow)
        self.actionDarkside.setObjectName("actionDarkside")
        self.actionWhiteside = QtWidgets.QAction(MainWindow)
        self.actionWhiteside.setObjectName("actionWhiteside")
        self.actionColorful_side = QtWidgets.QAction(MainWindow)
        self.actionColorful_side.setObjectName("actionColorful_side")
        self.actionYour_side = QtWidgets.QAction(MainWindow)
        self.actionYour_side.setObjectName("actionYour_side")
        self.actionNormal = QtWidgets.QAction(MainWindow)
        self.actionNormal.setObjectName("actionNormal")
        self.actionBold = QtWidgets.QAction(MainWindow)
        self.actionBold.setObjectName("actionBold")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDefault = QtWidgets.QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionGreen = QtWidgets.QAction(MainWindow)
        self.actionGreen.setObjectName("actionGreen")
        self.actionYellow = QtWidgets.QAction(MainWindow)
        self.actionYellow.setObjectName("actionYellow")
        self.actionBlue = QtWidgets.QAction(MainWindow)
        self.actionBlue.setObjectName("actionBlue")
        self.actionBlack = QtWidgets.QAction(MainWindow)
        self.actionBlack.setObjectName("actionBlack")
        self.actionWhite = QtWidgets.QAction(MainWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.menuBackground.addAction(self.actionDarkside)
        self.menuBackground.addAction(self.actionWhiteside)
        self.menuBackground.addAction(self.actionColorful_side)
        self.menuBackground.addAction(self.actionYour_side)
        self.menuTypescreen.addAction(self.actionNormal)
        self.menuTypescreen.addAction(self.actionBold)
        self.menuButton_Colour.addAction(self.actionDefault)
        self.menuButton_Colour.addAction(self.actionGreen)
        self.menuButton_Colour.addAction(self.actionYellow)
        self.menuButton_Colour.addAction(self.actionBlue)
        self.menuButton_Colour.addAction(self.actionBlack)
        self.menuButton_Colour.addAction(self.actionWhite)
        self.menuView.addAction(self.menuBackground.menuAction())
        self.menuView.addAction(self.menuTypescreen.menuAction())
        self.menuView.addAction(self.menuButton_Colour.menuAction())
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        '''Устанавливает текст и заголовки виджетов.'''
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Diary"))
        self.Month_year.setText(_translate("MainWindow", "Month and year"))
        self.Month_year.adjustSize() # Подогнать размера объекта под текущий монитор
        self.p2.setText(_translate("MainWindow", "PushButton"))
        self.p3.setText(_translate("MainWindow", "PushButton"))
        self.p4.setText(_translate("MainWindow", "PushButton"))
        self.p5.setText(_translate("MainWindow", "PushButton"))
        self.p1.setText(_translate("MainWindow", "PushButton"))
        self.p6.setText(_translate("MainWindow", "PushButton"))
        self.p7.setText(_translate("MainWindow", "PushButton"))
        self.p8.setText(_translate("MainWindow", "PushButton"))
        self.p9.setText(_translate("MainWindow", "PushButton"))
        self.p10.setText(_translate("MainWindow", "PushButton"))
        self.p11.setText(_translate("MainWindow", "PushButton"))
        self.p12.setText(_translate("MainWindow", "PushButton"))
        self.p13.setText(_translate("MainWindow", "PushButton"))
        self.p14.setText(_translate("MainWindow", "PushButton"))
        self.p21.setText(_translate("MainWindow", "PushButton"))
        self.p28.setText(_translate("MainWindow", "PushButton"))
        self.p35.setText(_translate("MainWindow", "PushButton"))
        self.p20.setText(_translate("MainWindow", "PushButton"))
        self.p27.setText(_translate("MainWindow", "PushButton"))
        self.p34.setText(_translate("MainWindow", "PushButton"))
        self.p19.setText(_translate("MainWindow", "PushButton"))
        self.p26.setText(_translate("MainWindow", "PushButton"))
        self.p33.setText(_translate("MainWindow", "PushButton"))
        self.p18.setText(_translate("MainWindow", "PushButton"))
        self.p25.setText(_translate("MainWindow", "PushButton"))
        self.p32.setText(_translate("MainWindow", "PushButton"))
        self.p17.setText(_translate("MainWindow", "PushButton"))
        self.p24.setText(_translate("MainWindow", "PushButton"))
        self.p31.setText(_translate("MainWindow", "PushButton"))
        self.p16.setText(_translate("MainWindow", "PushButton"))
        self.p23.setText(_translate("MainWindow", "PushButton"))
        self.p30.setText(_translate("MainWindow", "PushButton"))
        self.p22.setText(_translate("MainWindow", "PushButton"))
        self.p29.setText(_translate("MainWindow", "PushButton"))
        self.p15.setText(_translate("MainWindow", "PushButton"))
        self.Monday.setText(_translate("MainWindow", "Пн"))
        self.Tuesday.setText(_translate("MainWindow", "Вт"))
        self.Wednesday.setText(_translate("MainWindow", "Ср"))
        self.Thursday.setText(_translate("MainWindow", "Чт"))
        self.Friday.setText(_translate("MainWindow", "Пт"))
        self.Saturday.setText(_translate("MainWindow", "Сб"))
        self.Sunday.setText(_translate("MainWindow", "Вс"))
        self.p42.setText(_translate("MainWindow", "PushButton"))
        self.p41.setText(_translate("MainWindow", "PushButton"))
        self.p40.setText(_translate("MainWindow", "PushButton"))
        self.p39.setText(_translate("MainWindow", "PushButton"))
        self.p38.setText(_translate("MainWindow", "PushButton"))
        self.p37.setText(_translate("MainWindow", "PushButton"))
        self.p36.setText(_translate("MainWindow", "PushButton"))
        self.Left_step.setText(_translate("MainWindow", "Previous month"))
        self.Right_step.setText(_translate("MainWindow", "Next month"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuBackground.setTitle(_translate("MainWindow", "Background"))
        self.menuTypescreen.setTitle(_translate("MainWindow", "Typescreen"))
        self.menuButton_Colour.setTitle(_translate("MainWindow", "Button Colour"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionJanuary.setText(_translate("MainWindow", "January"))
        self.actionFebruary.setText(_translate("MainWindow", "February"))
        self.actionMarch.setText(_translate("MainWindow", "March"))
        self.actionApril.setText(_translate("MainWindow", "April"))
        self.actionMay.setText(_translate("MainWindow", "May"))
        self.actionJune.setText(_translate("MainWindow", "June"))
        self.actionJuly.setText(_translate("MainWindow", "July"))
        self.actionAugust.setText(_translate("MainWindow", "August"))
        self.actionSeptember.setText(_translate("MainWindow", "September"))
        self.actionOctober.setText(_translate("MainWindow", "October"))
        self.actionNovember.setText(_translate("MainWindow", "November"))
        self.actionDecember.setText(_translate("MainWindow", "December"))
        self.actionDarkside.setText(_translate("MainWindow", "DarkSide"))
        self.actionWhiteside.setText(_translate("MainWindow", "WhiteSide"))
        self.actionColorful_side.setText(_translate("MainWindow", "ColorfulSide"))
        self.actionYour_side.setText(_translate("MainWindow", "YourSide"))
        self.actionNormal.setText(_translate("MainWindow", "Normal"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionDefault.setText(_translate("MainWindow", "Default"))
        self.actionGreen.setText(_translate("MainWindow", "Green"))
        self.actionYellow.setText(_translate("MainWindow", "Orange"))
        self.actionBlue.setText(_translate("MainWindow", "Blue"))
        self.actionBlack.setText(_translate("MainWindow", "Black"))
        self.actionWhite.setText(_translate("MainWindow", "White"))

    def add_functions(self):
        '''Добавляет все необходимые функции для корректной работы приложения.'''
        self.set_month_and_date()
        self.set_dates()

        self.p1.clicked.connect(lambda: self.openWindow(self.p1.text()))
        self.p2.clicked.connect(lambda: self.openWindow(self.p2.text()))
        self.p3.clicked.connect(lambda: self.openWindow(self.p3.text()))
        self.p4.clicked.connect(lambda: self.openWindow(self.p4.text()))
        self.p5.clicked.connect(lambda: self.openWindow(self.p5.text()))
        self.p6.clicked.connect(lambda: self.openWindow(self.p6.text()))
        self.p7.clicked.connect(lambda: self.openWindow(self.p7.text()))
        self.p8.clicked.connect(lambda: self.openWindow(self.p8.text()))
        self.p9.clicked.connect(lambda: self.openWindow(self.p9.text()))
        self.p10.clicked.connect(lambda: self.openWindow(self.p10.text()))
        self.p11.clicked.connect(lambda: self.openWindow(self.p11.text()))
        self.p12.clicked.connect(lambda: self.openWindow(self.p12.text()))
        self.p13.clicked.connect(lambda: self.openWindow(self.p13.text()))
        self.p14.clicked.connect(lambda: self.openWindow(self.p14.text()))
        self.p15.clicked.connect(lambda: self.openWindow(self.p15.text()))
        self.p16.clicked.connect(lambda: self.openWindow(self.p16.text()))
        self.p17.clicked.connect(lambda: self.openWindow(self.p17.text()))
        self.p18.clicked.connect(lambda: self.openWindow(self.p18.text()))
        self.p19.clicked.connect(lambda: self.openWindow(self.p19.text()))
        self.p20.clicked.connect(lambda: self.openWindow(self.p20.text()))
        self.p21.clicked.connect(lambda: self.openWindow(self.p21.text()))
        self.p22.clicked.connect(lambda: self.openWindow(self.p22.text()))
        self.p23.clicked.connect(lambda: self.openWindow(self.p23.text()))
        self.p24.clicked.connect(lambda: self.openWindow(self.p24.text()))
        self.p25.clicked.connect(lambda: self.openWindow(self.p25.text()))
        self.p26.clicked.connect(lambda: self.openWindow(self.p26.text()))
        self.p27.clicked.connect(lambda: self.openWindow(self.p27.text()))
        self.p28.clicked.connect(lambda: self.openWindow(self.p28.text()))
        self.p29.clicked.connect(lambda: self.openWindow(self.p29.text()))
        self.p30.clicked.connect(lambda: self.openWindow(self.p30.text()))
        self.p31.clicked.connect(lambda: self.openWindow(self.p31.text()))
        self.p32.clicked.connect(lambda: self.openWindow(self.p32.text()))
        self.p33.clicked.connect(lambda: self.openWindow(self.p33.text()))
        self.p34.clicked.connect(lambda: self.openWindow(self.p34.text()))
        self.p35.clicked.connect(lambda: self.openWindow(self.p35.text()))
        self.p36.clicked.connect(lambda: self.openWindow(self.p36.text()))
        self.p37.clicked.connect(lambda: self.openWindow(self.p37.text()))
        self.p38.clicked.connect(lambda: self.openWindow(self.p38.text()))
        self.p39.clicked.connect(lambda: self.openWindow(self.p39.text()))
        self.p40.clicked.connect(lambda: self.openWindow(self.p40.text()))
        self.p41.clicked.connect(lambda: self.openWindow(self.p41.text()))
        self.p42.clicked.connect(lambda: self.openWindow(self.p42.text()))

        self.actionDarkside.triggered.connect(lambda: self.change_background(self.actionDarkside.text()))
        self.actionWhiteside.triggered.connect(lambda: self.change_background(self.actionWhiteside.text()))
        self.actionColorful_side.triggered.connect(lambda: self.change_background(self.actionColorful_side.text()))
        self.actionYour_side.triggered.connect(lambda: self.change_background(self.actionYour_side.text()))

        self.actionBold.triggered.connect(lambda: self.change_font(self.actionBold.text()))
        self.actionNormal.triggered.connect(lambda: self.change_font(self.actionNormal.text()))

        self.actionExit.triggered.connect(lambda: self.exit_app())

    def openWindow(self, opened_day):
        '''Открывает окно SecondWindow.py при нажатии на кнопку в календаре.'''
        currentMonth = datetime.now().month
        currentYear = datetime.now().strftime("%Y")
        date = currentYear + '-' + str(currentMonth) + '-' + opened_day
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window, date)
        self.window.show()

    def change_background(self, background):
        '''Меняет задний фон приложения.'''
        if background == "Darkside":
            self.label.setPixmap(QtGui.QPixmap())
            self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.Month_year.setStyleSheet("color: rgb(255, 255, 255)");
        elif background == "White side":
            self.label.setPixmap(QtGui.QPixmap())
            self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.Month_year.setStyleSheet("color: rgb(0, 0, 0)");
        elif background == "Colorful side":
            self.label.setPixmap(QtGui.QPixmap("D:/Загрузки/background_of_diary.jpg"))
            self.Month_year.setStyleSheet("color: rgb(0, 0, 0)");
        elif background == "Your side":
            new_background = QFileDialog.getOpenFileName()[0]
            self.label.setPixmap(QtGui.QPixmap(new_background))
            self.Month_year.setStyleSheet("color: rgb(255, 255, 255)");

    def change_font(self, font):
        '''Меняет шрифт в приложении.'''
        if font == "Bold":
            if self.get_backgroud_color() == "#000000":
                self.Month_year.setStyleSheet("font-weight: bold; color: rgb(255, 255, 255)");
            else:
                self.Month_year.setStyleSheet("font-weight: bold; color: rgb(0, 0, 0)");
            self.Monday.setStyleSheet("font-weight: bold");
            self.Tuesday.setStyleSheet("font-weight: bold");
            self.Wednesday.setStyleSheet("font-weight: bold");
            self.Thursday.setStyleSheet("font-weight: bold");
            self.Friday.setStyleSheet("font-weight: bold");
            self.Saturday.setStyleSheet("font-weight: bold");
            self.Sunday.setStyleSheet("font-weight: bold");
        elif font == "Normal":
            if self.get_backgroud_color() == "#000000":
                self.Month_year.setStyleSheet("font-weight: normal; color: rgb(255, 255, 255)");
            else:
                self.Month_year.setStyleSheet("font-weight: normal; color: rgb(0, 0, 0)");
            self.Monday.setStyleSheet("font-weight: normal");
            self.Tuesday.setStyleSheet("font-weight: normal");
            self.Wednesday.setStyleSheet("font-weight: normal");
            self.Thursday.setStyleSheet("font-weight: normal");
            self.Friday.setStyleSheet("font-weight: normal");
            self.Saturday.setStyleSheet("font-weight: normal");
            self.Sunday.setStyleSheet("font-weight: normal");

    def get_backgroud_color(self):
        '''Возвращает цвет заднего фона.'''
        return self.label.palette().window().color().name()

    def exit_app(self):
        '''Функция для выхода из приложения путем нажатия кнопки.'''
        sys.exit()

    def set_month_and_date(self, currentMonth = datetime.now().strftime("%B"), currentYear = datetime.now().year):
        '''Устанавливает текущие год и месяц.'''
        currentMonth = datetime.now().strftime("%B")
        currentYear = datetime.now().strftime("%Y")
        self.Month_year.setText(currentMonth + ' ' + currentYear)

    def set_dates(self, currentMonth = datetime.now().month, currentYear = datetime.now().year):
        '''Устанавливает даты на кнопки в календаре.'''
        mrange = monthrange(currentYear, currentMonth)

        for i in range(1, mrange[1] + 1):
            eval("self.p{}.setText(\"{}\")".format(i + mrange[0], str(i)))
        for i in range(1, mrange[0] + 1):
            eval("self.p{}.setVisible(False)".format(i))
        for i in range(mrange[0] + mrange[1] + 1, 43):
            eval("self.p{}.setVisible(False)".format(i))

    def openWindow(self, opened_day):
        '''Открывает окно SecondWindow.py при нажатии на кнопку в календаре.'''
        current_datetime = datetime.now()
        currentMonth = datetime.now().month
        currentYear = current_datetime.strftime("%Y")
        date = currentYear + '-' + str(currentMonth) + '-' + opened_day
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window, date)
        self.window.show()

    def change_background(self, background):
        '''Меняет задний фон приложения.'''
        if background == "DarkSide":
            self.label.setPixmap(QtGui.QPixmap())
            self.label.setStyleSheet("background-color: rgb(0, 0, 0);")
            self.Month_year.setStyleSheet("color: rgb(255, 255, 255)");
        elif background == "WhiteSide":
            self.label.setPixmap(QtGui.QPixmap())
            self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
            self.Month_year.setStyleSheet("color: rgb(0, 0, 0)");
        elif background == "ColorfulSide":
            self.label.setPixmap(QtGui.QPixmap("D:/Загрузки/background_of_diary.jpg"))
            self.Month_year.setStyleSheet("color: rgb(0, 0, 0)");
        elif background == "YourSide":
            new_background = QFileDialog.getOpenFileName()[0]
            self.label.setPixmap(QtGui.QPixmap(new_background))
            self.Month_year.setStyleSheet("color: rgb(255, 255, 255)");

    def change_font(self, font):
        '''Меняет шрифт в приложении.'''
        if font == "Bold":
            if self.get_backgroud_color() == "#000000":
                self.Month_year.setStyleSheet("font-weight: bold; color: rgb(255, 255, 255)");
            else:
                self.Month_year.setStyleSheet("font-weight: bold; color: rgb(0, 0, 0)");
            self.Monday.setStyleSheet("font-weight: bold");
            self.Tuesday.setStyleSheet("font-weight: bold");
            self.Wednesday.setStyleSheet("font-weight: bold");
            self.Thursday.setStyleSheet("font-weight: bold");
            self.Friday.setStyleSheet("font-weight: bold");
            self.Saturday.setStyleSheet("font-weight: bold");
            self.Sunday.setStyleSheet("font-weight: bold");
        elif font == "Normal":
            if self.get_backgroud_color() == "#000000":
                self.Month_year.setStyleSheet("font-weight: normal; color: rgb(255, 255, 255)");
            else:
                self.Month_year.setStyleSheet("font-weight: normal; color: rgb(0, 0, 0)");
            self.Monday.setStyleSheet("font-weight: normal");
            self.Tuesday.setStyleSheet("font-weight: normal");
            self.Wednesday.setStyleSheet("font-weight: normal");
            self.Thursday.setStyleSheet("font-weight: normal");
            self.Friday.setStyleSheet("font-weight: normal");
            self.Saturday.setStyleSheet("font-weight: normal");
            self.Sunday.setStyleSheet("font-weight: normal");

    def get_backgroud_color(self):
        '''Возвращает цвет заднего фона.'''
        return self.label.palette().window().color().name()

    def exit_app(self):
        '''Функция для выхода из приложения путем нажатия кнопки.'''
        sys.exit()

    def set_month_and_date(self):
        '''Устанавливает текущие год и месяц.'''
        currentMonth = datetime.now().strftime("%B")
        currentYear = datetime.now().strftime("%Y")
        self.Month_year.setText(currentMonth + ' ' + currentYear)

    def set_dates(self, currentMonth = datetime.now().month, currentYear = datetime.now().year):
        '''Устанавливает даты на кнопки в календаре.'''
        mrange = monthrange(currentYear, currentMonth)

        for i in range(1, mrange[1] + 1):
            eval("self.p{}.setText(\"{}\")".format(i + mrange[0], str(i)))
        for i in range(1, mrange[0] + 1):
            eval("self.p{}.setVisible(False)".format(i))
        for i in range(mrange[0] + mrange[1] + 1, 43):
            eval("self.p{}.setVisible(False)".format(i))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
