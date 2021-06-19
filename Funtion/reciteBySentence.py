import random
import re
from time import sleep

from BaiduApiAccess.TTS_STT import say, listen
from DataAccess.PassageAccess import getCHNPassageTitles, getCHNPassageById

#  参数为主循环中的client
#  整体应当为一个循环，直到用户不想继续本功能再返回
def recite_by_sentence():
    say("好的，开始逐句跟背")

    # 询问要背哪首诗
    titles = getCHNPassageTitles()
    passage_id=random.choice(list(titles.values()))
    say("请问你要背哪首诗")
    text=listen().replace('。','')
    # text=input("输入诗的题目：")
    if text in titles.keys():
        passage_id=titles[text]
    else:
        say("没有您要背的诗哦，我们随机背一首吧")

    passage=getCHNPassageById(passage_id)
    # print(passage)
    say(passage['title'])
    say(passage['writer'])
    sentences=re.split('，|。|,|\.',passage['content'])
    for s in sentences:
        while True:
            say(s)
            ans=listen().replace('。','')
            # ans=input()
            if s in ans:
                break
            else:
                say("不对哦，再来一遍")
    say("跟背完毕")


if __name__=="__main__":
    recite_by_sentence()
