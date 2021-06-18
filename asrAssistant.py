import os
from PyQt5 import QtWidgets, QtCore
import _thread
from asrInterface import Ui_MainWindow
import sys
from playsound import playsound
from datetime import datetime
import speech_recognition as sr
from aip import AipSpeech
import question
import game
import reciteWhole
import reciteBySentence
from TTS_STT import say, listen
from xpinyin import Pinyin

def running():
    flag = False
    while True:
        request = listen()
        print("I heard: " + request)

        if flag:
            flag = False
            if request.find("背课文") != -1:
                application.ui.call_backlog("背课文!")
                reciteWhole.recite_whole()
            elif request.find("跟背") != -1:
                application.ui.call_backlog("逐句跟背!")
                reciteBySentence.recite_by_sentence()
            elif request.find("游戏") != -1:
                application.ui.call_backlog("游戏!")
                game.play_game()
            elif request.find("题") != -1:
                application.ui.call_backlog("做题!")
                question.answer_questions()
            else:
                flag = True
                sentence = "对不起，我没听懂你想做什么，可以再说一遍吗"
                say(sentence)

        else:
            if  Pinyin().get_pinyin(request, ' ').find("yu di") != -1:
                say('你好，我是语滴，请问你想做什么')
                print("唤醒！")
                flag = True


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        _thread.start_new_thread(running, ())
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()
sys.exit(app.exec())
