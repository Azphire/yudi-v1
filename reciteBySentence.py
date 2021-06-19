import random
from time import sleep

from BaiduApiAccess.TTS_STT import say, listen
from DataAccess.PassageAccess import getCHNPassageTitles, getCHNPassageById

#  参数为主循环中的client
#  整体应当为一个循环，直到用户不想继续本功能再返回
def recite_by_sentence():
    say("好的，开始逐句跟背")
    sleep(1)

    # 询问要背哪首诗
    titles = getCHNPassageTitles()
    passageId=random.choice(titles.values())
    say("请问你要背哪首诗")
    text=listen()
    if text in titles.keys():
        passageId=titles[text]
    else:
        say("没有您要背的诗哦，我们随机背一首吧")

    passage=getCHNPassageById(passageId)
    print(passage)

if __name__=="__main__":
    recite_by_sentence()
