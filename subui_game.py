# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie,QIcon
import qtawesome
import sys
class SubUi_game(object):
    def setupUi(self,Dialog):
        Dialog.setFixedSize(350, 600)
        Dialog.setObjectName("Dialog")
        #Dialog.setStyleSheet("border-radius:10px;")

        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);border-radius:10px;")
        
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(10, 10, 90, 40))
        self.back_button.setIcon(QIcon(qtawesome.icon('fa.chevron-left',color='white')))
        self.back_button.setText("返回主页")
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: white;")
        self.back_button.setObjectName("back_button")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 200, 350, 21))
        self.label.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(0, 240, 350, 21))
        self.label_1.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_1.setTextFormat(QtCore.Qt.AutoText)
        self.label_1.setWordWrap(True)
        self.label_1.setObjectName("label_1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 280, 350, 21))
        self.label_2.setAlignment(Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 117, 210);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")


        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(105, 450, 140, 100))
        self.voiceFig.setAlignment(Qt.AlignCenter)
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        
        #Dialog.setCentralWidget(self.centralwidget)

        #self.statusbar = QtWidgets.QStatusBar(Dialog)
        #self.statusbar.setObjectName("statusbar")
        #Dialog.setStatusBar(self.statusbar)

        Dialog.setAttribute(Qt.WA_TranslucentBackground) # 设置窗口背景透明
        Dialog.setWindowFlag(Qt.FramelessWindowHint) # 隐藏边框

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "语滴助手"))
        self.label.setText(_translate("Dialog", "欢迎进入"))
        self.label_1.setText(_translate("Dialog", "三体剧情游戏"))
        self.label_2.setText(_translate("Dialog", "请加油走到游戏最后"))

# class subWindow_two(QtWidgets.QDialog):

#     def __init__(self):
#         super(subWindow_two, self).__init__()
#         self.ui = SubUi_two()
#         self.ui.init_ui(self)

# app = QtWidgets.QApplication([])
# application = subWindow_two()
# application.show()
# sys.exit(app.exec())
