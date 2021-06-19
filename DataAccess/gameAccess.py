from DataAccess.connection import MySQLConnection
import json

def trans2Game(info):
    m={}
    m['id']=info[0]
    m['intro']=info[1]
    m['title']=info[2]
    m['startPlot'] = info[3]
    return m

def trans2GamePlot(info):
    m={}
    m['gameId']=info[0]
    m['plotId']=info[1]
    m['content']=info[2]
    m['isEnding']=info[3]
    m['choices']=json.loads(info[4])
    return m

def getGames():
    conn=MySQLConnection()
    sqli="select * from Game;"
    res=[]
    infos=conn.select_record(sqli)
    if infos['status']==200:
        infos=infos['data']
        for info in infos:
            r=trans2Game(info)
            res.append(r)
    return res

def getGameByTitle(title):
    conn = MySQLConnection()
    if ~isinstance(title,str):
        title=str(title)
    sqli = "select * from Game where title like \"%" + title + "%\""
    info = conn.select_record(sqli)
    if info['status'] == 200:
        info = info['data'][0]
        return trans2Game(info)

def getGamePlot(id):
    conn = MySQLConnection()
    if ~isinstance(id,str):
        id=str(id)
    sqli = "select * from GamePlot where plotId=" + id
    info = conn.select_record(sqli)
    if info['status'] == 200:
        info = info['data'][0]
        return trans2GamePlot(info)

if __name__=="__main__":
    print(getGames())
    print(getGameByTitle("黑暗森林"))
    plot = getGamePlot(1)
    print(plot["choices"])
    for k,v in plot["choices"].items():
        print(k,v)