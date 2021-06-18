from playsound import playsound
import os


#  参数为主循环中的client
# 整体应当为循环，直到用户不想继续本功能再返回
def answer_questions(client):
    result = client.synthesis("好的，现在开始做题", 'zh', 1, {
        'vol': 5, 'per': 0, 'spd': 5
    })
    if not isinstance(result, dict):
        with open('audio.mp3', 'wb') as f:
            f.write(result)
    playsound("audio.mp3")
    os.remove("audio.mp3")
