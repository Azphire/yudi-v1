from TTS_STT import say, listen


#  参数为主循环中的client
#  整体应当为一个循环，直到用户不想继续本功能再返回
def recite_by_sentence():
    say("好的，开始逐句跟背")
