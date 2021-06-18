import os
from playsound import playsound
from aip import AipSpeech
import speech_recognition as sr

# Baidu Speech API
APP_ID = '24398244'
API_KEY = 'tvMrgpcmEeKiAPDWfhAG0EKl'
SECRET_KEY = '4OHO7ClRWVKgi7S9mgkK4P5oSINFki0W'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def say(sentence):
    result = client.synthesis(sentence, 'zh', 1, {
        'vol': 5, 'per': 0, 'spd': 5
    })
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
    playsound("audio.mp3")
    os.remove("audio.mp3")


# Use SpeechRecognition to record
def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        audio = r.listen(source)

    with open("temp.wav", "wb") as f:
        # 此处将录音文件存储为temp.wav供后续语音识别取用，识别结束后会将文件删除
        f.write(audio.get_wav_data())


def listen():
    rec()
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