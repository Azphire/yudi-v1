from DataAccess.connection import MySQLConnection

def trans2CHNQuestion(info):
    m={}
    m['id']=info[0]
    m['question']=info[1]
    m['answer']=info[2]
    m['grade']=info[3]
    return m

def getCHNQuestions():
    conn=MySQLConnection()
    sqli="select * from CHNQuestion;"
    res=[]
    infos=conn.select_record(sqli)
    if infos['status']==200:
        infos=infos['data']
        for info in infos:
            r=trans2CHNQuestion(info)
            res.append(r)
    return res

def getCHNQuestionByGrade(grade):
    conn = MySQLConnection()
    if ~isinstance(grade,str):
        grade=str(grade)
    sqli = "select * from CHNQuestion where grade="+grade
    info = conn.select_record(sqli)
    if info['status'] == 200:
        info = info['data'][0]
        return trans2CHNQuestion(info)

if __name__=="__main__":
    # passages=getCHNPassages()
    # for p in passages:
    #     print(p)

    # titles=getCHNPassageTitles()
    # for t in titles.keys():
    #     print(t,titles[t])

    print(getCHNQuestionByGrade(6))