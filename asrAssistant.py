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

# Baidu Speech API
APP_ID = '24398244'
API_KEY = 'tvMrgpcmEeKiAPDWfhAG0EKl'
SECRET_KEY = '4OHO7ClRWVKgi7S9mgkK4P5oSINFki0W'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


# Use SpeechRecognition to record
def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        application.ui.call_backlog("I'm listening")  # 回调改状态
        print("please say something")
        audio = r.listen(source)
        application.ui.call_backlog("Recognizing...")

    with open("temp.wav", "wb") as f:
        # 此处将录音文件存储为temp.wav供后续语音识别取用，识别结束后会将文件删除
        f.write(audio.get_wav_data())


# Use Baidu Speech as STT engine
def listen():
    with open('temp.wav', 'rb') as f:
        audio_data = f.read()

    #  删除临时音频文件
    os.remove('temp.wav')

    # 获取语音识别api结果
    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1537,
    })

    # 提取出识别文本
    try:
        result_text = result["result"][0]
        return result_text

    except:
        return "error"


def running():
    flag = False
    while True:
        rec()
        request = listen()
        print("I heard: " + request)

        if flag:
            flag = False
            if request.find("背课文") != -1:
                application.ui.call_backlog("背课文!")
                reciteWhole.recite_whole(client)
            elif request.find("跟背") != -1:
                application.ui.call_backlog("逐句跟背!")
                reciteBySentence.recite_by_sentence(client)
            elif request.find("游戏") != -1:
                application.ui.call_backlog("游戏!")
                game.play_game(client)
            elif request.find("题") != -1:
                application.ui.call_backlog("做题!")
                question.answer_questions(client)
            else:
                flag = True
                sentence = "对不起，我没听懂你想做什么，可以再说一遍吗"
                result = client.synthesis(sentence, 'zh', 1, {
                    'vol': 5, 'per': 0, 'spd': 5
                })
                if not isinstance(result, dict):
                    with open('audio.mp3', 'wb') as f:
                        f.write(result)
                playsound("audio.mp3")
                os.remove("audio.mp3")

        else:
            if request.find("雨滴") != -1:
                result = client.synthesis('你好，我是语滴，请问你想做什么', 'zh', 1, {
                    'vol': 5, 'per': 0, 'spd': 5
                })
                if not isinstance(result, dict):
                    with open('audio.mp3', 'wb') as f:
                        f.write(result)
                playsound("audio.mp3")
                os.remove("audio.mp3")
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
