# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JailSpyder.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(615, 327)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setIndent(0)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 0, 1, 5)
        self.pushButton_luck = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_luck.setObjectName("pushButton_luck")
        self.gridLayout.addWidget(self.pushButton_luck, 1, 0, 1, 1)
        self.GuideJ = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.GuideJ.setFont(font)
        self.GuideJ.setAlignment(QtCore.Qt.AlignCenter)
        self.GuideJ.setIndent(0)
        self.GuideJ.setObjectName("GuideJ")
        self.gridLayout.addWidget(self.GuideJ, 1, 1, 1, 1)
        self.lineEdit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.gridLayout.addWidget(self.lineEdit_input, 1, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 3, 1, 1)
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.pushButton_search.setFont(font)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout.addWidget(self.pushButton_search, 1, 4, 1, 1)
        self.textBrowser_luck = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_luck.setObjectName("textBrowser_luck")
        self.gridLayout.addWidget(self.textBrowser_luck, 2, 0, 1, 1)
        self.cover = QtWidgets.QLabel(self.centralwidget)
        self.cover.setAlignment(QtCore.Qt.AlignCenter)
        self.cover.setObjectName("cover")
        self.gridLayout.addWidget(self.cover, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(0)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 4)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 4, 1, 1)
        self.textBrowser_res = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_res.setObjectName("textBrowser_res")
        self.gridLayout.addWidget(self.textBrowser_res, 2, 2, 2, 3)
        self.textBrowser_GuideJ = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_GuideJ.setObjectName("textBrowser_GuideJ")
        self.gridLayout.addWidget(self.textBrowser_GuideJ, 2, 1, 2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 22))
        self.menubar.setObjectName("menubar")
        self.menuHello_Spy = QtWidgets.QMenu(self.menubar)
        self.menuHello_Spy.setObjectName("menuHello_Spy")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHello_Spy.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title.setText(_translate("MainWindow", "豆瓣电影Top250检索系统"))
        self.pushButton_luck.setText(_translate("MainWindow", "手气不错"))
        self.GuideJ.setText(_translate("MainWindow", "助理小J"))
        self.comboBox.setItemText(0, _translate("MainWindow", "模糊搜索"))
        self.comboBox.setItemText(1, _translate("MainWindow", "全名搜索"))
        self.comboBox.setItemText(2, _translate("MainWindow", "类别搜索"))
        self.comboBox.setItemText(3, _translate("MainWindow", "导演搜索"))
        self.comboBox.setItemText(4, _translate("MainWindow", "主演搜索"))
        self.comboBox.setItemText(5, _translate("MainWindow", "排名搜索"))
        self.comboBox.setItemText(6, _translate("MainWindow", "排名范围"))
        self.comboBox.setItemText(7, _translate("MainWindow", "评分搜索"))
        self.comboBox.setItemText(8, _translate("MainWindow", "评分范围"))
        self.comboBox.setItemText(9, _translate("MainWindow", "年份搜索"))
        self.comboBox.setItemText(10, _translate("MainWindow", "年份范围"))
        self.pushButton_search.setText(_translate("MainWindow", "检索一下"))
        self.cover.setText(_translate("MainWindow", "好运在此！"))
        self.label_5.setText(_translate("MainWindow", "Copyright@JailSpyder 🕷-∞  All Rights Reserved"))
        self.pushButton.setText(_translate("MainWindow", "Exit"))
        self.menuHello_Spy.setTitle(_translate("MainWindow", "JailSpyder"))
