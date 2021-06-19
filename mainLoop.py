from PyQt5 import QtWidgets
import _thread
from asrInterface import Ui_MainWindow
import sys
from Function import game, question, reciteWhole, reciteBySentence
from BaiduApiAccess.TTS_STT import say, listen
from xpinyin import Pinyin

def running():
    flag = False
    while True:
        request = listen(ding=False)

        if flag:
            flag = False
            if request.find("背课文") != -1:
                reciteWhole.recite_whole()
            elif request.find("跟背") != -1:
                reciteBySentence.recite_by_sentence()
            elif request.find("游戏") != -1:
                game.play_game()
            elif request.find("问答") != -1:
                question.answer_questions()
            else:
                flag = True
                sentence = "对不起，我没听懂你想做什么，可以再说一遍吗"
                say(sentence)

        else:
            if Pinyin().get_pinyin(request, ' ').find("yu di") != -1:
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
