from DataAccess.connection import MySQLConnection

def trans2CHNPassage(info):
    m={}
    m['id']=info[0]
    m['title']=info[1]
    m['writer']=info[2]
    m['grade']=info[3]
    m['version']=info[4]
    m['content']=info[5]
    return m

def getCHNPassages():
    conn=MySQLConnection()
    sqli="select * from CHNPassage;"
    res=[]
    infos=conn.select_record(sqli)
    if infos['status']==200:
        infos=infos['data']
        for info in infos:
            r=trans2CHNPassage(info)
            res.append(r)
    return res

def getCHNPassageTitles():
    conn=MySQLConnection()
    sqli="select CHNPassageID,title from CHNPassage;"
    res={}
    infos = conn.select_record(sqli)
    if infos['status'] == 200:
        infos = infos['data']
        for info in infos:
            res[info[1]]=info[0]
    return res

def getCHNPassageById(id):
    conn = MySQLConnection()
    if ~isinstance(id,str):
        id=str(id)
    sqli = "select * from CHNPassage where CHNPassageID="+id
    info = conn.select_record(sqli)
    if info['status'] == 200:
        info = info['data'][0]
        return trans2CHNPassage(info)

if __name__=="__main__":
    # passages=getCHNPassages()
    # for p in passages:
    #     print(p)

    # titles=getCHNPassageTitles()
    # for t in titles.keys():
    #     print(t,titles[t])

    print(getCHNPassageById(1))