from BaiduApiAccess.TTS_STT import say


#  参数为主循环中的client
#  整体应当为一个循环，直到用户不想继续本功能再返回
def recite_whole():
    say("好的，开始背诵全文")
