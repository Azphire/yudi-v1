from PyQt5 import QtWidgets
import _thread
import sys
from Function import game, question, reciteWhole, reciteBySentence
from BaiduApiAccess.TTS_STT import say, listen
from xpinyin import Pinyin

# TODO: 逐句跟背的识别，audio的命名
def running():
    flag = False
    while True:
        
        request = listen(ding=False)
        print("主线程在运行。")
        if flag:
            flag = False
            if request.find("背课文") != -1:
                reciteWhole.recite_whole()
            elif Pinyin().get_pinyin(request, ' ').find("gen bei") != -1:
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

