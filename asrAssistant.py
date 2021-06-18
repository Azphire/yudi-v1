import os
from PyQt5 import QtWidgets, QtCore
import _thread
from asrInterface import Ui_MainWindow
import sys
from playsound import playsound
from datetime import datetime
import speech_recognition as sr
from aip import AipSpeech

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


def play_music():
    playsound("music.mp3")


def open_notepad():
    time = datetime.now()
    file = 'note' + time.strftime('%Y%m%d%H%M%S') + '.txt'
    with open(file, 'w+') as f:
        print('记录于：\n' + time.strftime('%Y-%m-%d %H:%M:%S'), file=f)
    os.system(file)


def take_record(record):
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    with open('record' + time + '.txt', 'w+') as f:
        f.write(record)
        f.close()


def running():
    while True:
        rec()
        request = listen()
        print("I heard: " + request)

        if request.lower().find("记录") != -1:
            application.ui.call_backlog("Already taken down!")
            take_record(request)
        elif request.lower().find("雨滴") != -1:
            result = client.synthesis('Hi，我是语滴', 'zh', 1, {
                'vol': 5,
            })
            if not isinstance(result, dict):
                with open('audio.mp3', 'wb') as f:
                    f.write(result)
            playsound("audio.mp3")
            print("唤醒！")
            # application.ui.call_backlog("Playing music!")
            # play_music()
        elif request.lower().find("打开记事本") != -1:
            application.ui.call_backlog("Open Notepad!")
            open_notepad()
        else:
            application.ui.call_backlog("I didn’t catch you.")


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
