from homeui import*
from subui_one import*
from subui_two import*
from subui_three import*
import Funtion.reciteBySentence as rs
import Funtion.game as gm
import Funtion.question as qa
import Funtion.reciteWhole as rw
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QMessageBox
import os
from PyQt5.QtCore import pyqtSignal,QThread
import sys
import _thread

class function_one(QThread):
    signal1 = pyqtSignal()    # 括号里填写信号传递的参数
    def __init__(self):
        super().__init__()
    def __del__(self):
        self.wait()
    def run(self):
        # 进行任务操作
        rs.recite_by_sentence()
        self.signal1.emit()    # 发射信号

class function_two(QThread):
    signal2 = pyqtSignal()    # 括号里填写信号传递的参数
    def __init__(self):
        super().__init__()
    def __del__(self):
        self.wait()

    def run(self):
        # 进行任务操作
        rw.recite_whole()
        self.signal2.emit()    # 发射信号

class function_three(QThread):
    signal3 = pyqtSignal()    # 括号里填写信号传递的参数
    def __init__(self):
        super().__init__()
    def __del__(self):
        self.wait()

    def run(self):
        # 进行任务操作
        qa.answer_questions()
        self.signal3.emit()    # 发射信号

class function_game(QThread):
    signal4 = pyqtSignal()    # 括号里填写信号传递的参数
    def __init__(self):
        super().__init__()
    def __del__(self):
        self.wait()
    def run(self):
        # 进行任务操作
        gm.play_game()
        self.signal4.emit()    # 发射信号



class mainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = MainUi()
        self.ui.setupUi(self)
        self.ui.left_button_1.clicked.connect(self.showsubone)
        self.ui.left_button_2.clicked.connect(self.showsubtwo)
        self.ui.left_button_3.clicked.connect(self.showsubthree)
        self.ui.playlist_button_1.clicked.connect(self.showsubgame)
        self.ui.left_close.clicked.connect(self.iclose)
        
    def showmain(self):
        self.setVisible(1)#显示主界面
    def callback(self):
        pass
    def showsubone(self):
        self.subone = subWindow_one()
        self.subone.backsignal1.connect(self.showmain)
        self.setVisible(0)
        self.subone.setVisible(1)
        #self.subone.running()
        self.thread_one = function_one()
        self.thread_one.signal1.connect(self.callback)
        self.thread_one.start()    # 启动线程
    
    def showsubtwo(self):
        self.subtwo = subWindow_two()
        self.subtwo.backsignal2.connect(self.showmain)
        self.setVisible(0)
        self.subtwo.setVisible(1)
        self.thread_two = function_two()
        self.thread_two.signal2.connect(self.callback)
        self.thread_two.start()

    def showsubthree(self):
        self.subthree = subWindow_three()
        self.subthree.backsignal3.connect(self.showmain)
        self.setVisible(0)
        self.subthree.setVisible(1)
        self.thread_three = function_three()
        self.thread_three.signal3.connect(self.callback)
        self.thread_three.start()

    def showsubgame(self):
        self.subgame = subWindow_game()
        self.subgame.backsignal4.connect(self.showmain)
        self.setVisible(0)
        self.subgame.setVisible(1)
        self.thread_game = function_game()
        self.thread_game.signal4.connect(self.callback)
        self.thread_game.start()


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
    def running(self):
        for i in range(1000):
            if i%100 != 0:
                print(i)

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

class subWindow_game(QDialog):
    backsignal4 = pyqtSignal()
    def __init__(self):
        QDialog.__init__(self)
        self.ui = SubUi_three()
        self.ui.setupUi(self)
        self.ui.back_button.clicked.connect(self.backmain)
    def backmain(self):
        self.backsignal4.emit()#发送返回信号
        self.setVisible(0)

if __name__=='__main__':
    app=QApplication(sys.argv)
    home=mainWindow()
    home.show()
    sys.exit(app.exec_())
    # 显示