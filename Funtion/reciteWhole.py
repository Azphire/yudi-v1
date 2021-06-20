import random
import re
import  difflib
from pprint import pprint

from BaiduApiAccess.TTS_STT import say,listen
from DataAccess.PassageAccess import getCHNPassageTitles,getCHNPassageById

BIAODIAN='，|。|？|！|、|,|\.|?|!'

def getErrMsg(text1,text2):
    m={'-':[],'+':[],'?':[]}
    diff = difflib.Differ()
    d = list(diff.compare(text1, text2))
    i=0
    size=len(d)
    while i<size:
        tag=False
        c=d[i][0]
        if c in ['+','-']:
            if i+1<size and d[i+1][0]=='?':
                tag=True
            else:
                m[c].append(d[i][2:])
        if tag:
            m['?'].append((d[i][2:],d[i+2][2:]))
            i+=4
        else:
            i+=1
    return m

#  参数为主循环中的client
#  整体应当为一个循环，直到用户不想继续本功能再返回
def recite_whole():
    say("好的，开始背诵全文")
    # 询问要背哪首诗
    titles = getCHNPassageTitles()
    passage_id = random.choice(list(titles.values()))
    say("请问你要背哪首诗")
    text = listen().replace('。', '')
    # text=input("输入诗的题目：")
    if text in titles.keys():
        passage_id = titles[text]
    else:
        say("没有您要背的诗哦，我们随机背一首吧")

    passage = getCHNPassageById(passage_id)
    # print(passage)
    say(passage['title'])
    say(passage['writer'])
    say("预备，开始：")
    ans=listen()
    say("背诵完毕，正在解析")
    ans=[s for s in re.split(BIAODIAN, ans) if s.strip()!='']
    sentences = [s for s in re.split(BIAODIAN, passage['content']) if s.strip()!='']
    res=getErrMsg(sentences,ans)
    say("解析完毕")
    if len(res['?'])>0:
        say("以下为背错的部分：")
        for s in res['?']:
            say("应为："+s[0])
            say("背为："+s[1])
    if len(res['-'])>0:
        say("以下为漏背的部分："+",".join(res['-']))
    if len(res['+'])>0:
        say("以下为多余的部分："+",".join(res['+']))
    if len(res['-'])==0 and len(res['+'])==0 and len(res['?'])==0:
        say("恭喜你！没有错误！")

if __name__ == "__main__":
    recite_whole()
