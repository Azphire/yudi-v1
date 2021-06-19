from homeui import*
from subui_one import*
from subui_two import*
from subui_three import*
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QMessageBox
import os
from PyQt5.QtCore import pyqtSignal
import sys

class mainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainUi()
        self.ui.setupUi(self)
        self.ui.left_button_1.clicked.connect(self.showsubone)
        self.ui.left_button_2.clicked.connect(self.showsubtwo)
        self.ui.left_button_3.clicked.connect(self.showsubthree)
        self.ui.left_close.clicked.connect(self.iclose)
        self.subone = subWindow_one()
        self.subtwo = subWindow_two()
        self.subthree = subWindow_three()
        self.subone.backsignal1.connect(self.showmain)
        self.subtwo.backsignal2.connect(self.showmain)
        self.subthree.backsignal3.connect(self.showmain)

    def showmain(self):
        self.setVisible(1)#显示主界面

    def showsubone(self):
        self.setVisible(0)
        self.subone.setVisible(1)
    
    def showsubtwo(self):
        self.setVisible(0)
        self.subtwo.setVisible(1)
    
    def showsubthree(self):
        self.setVisible(0)
        self.subthree.setVisible(1)
    
    def iclose(self):
        os._exit(0)

class subWindow_one(QDialog):
    backsignal1 = pyqtSignal()
    def __init__(self):
        QDialog.__init__(self)
        self.ui = SubUi_one()
        self.ui.setupUi(self)
        self.ui.back_button.clicked.connect(self.backmain)
    def backmain(self):
        self.backsignal1.emit()#发送返回信号
        self.setVisible(0)


class subWindow_two(QDialog):
    backsignal2 = pyqtSignal()
    def __init__(self):
        QDialog.__init__(self)
        self.ui = SubUi_two()
        self.ui.setupUi(self)
        self.ui.back_button.clicked.connect(self.backmain)
    def backmain(self):
        self.backsignal2.emit()#发送返回信号
        self.setVisible(0)#关闭界面

class subWindow_three(QDialog):
    backsignal3 = pyqtSignal()
    def __init__(self):
        QDialog.__init__(self)
        self.ui = SubUi_three()
        self.ui.setupUi(self)
        self.ui.back_button.clicked.connect(self.backmain)
    def backmain(self):
        self.backsignal3.emit()#发送返回信号
        self.setVisible(0)

if __name__=='__main__':
    app=QApplication(sys.argv)
    home=mainWindow()
    home.show()
    sys.exit(app.exec_())
    # 显示