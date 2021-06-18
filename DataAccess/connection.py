import pymysql
HOST='121.199.77.139'
PORT=3306
USER='yudi'
PASSWORD='123'
DB='Yudi'
CHARSET='utf8mb4'

class MySQLConnection(object):
    def __init__(self,host=HOST,user=USER,port=PORT,password=PASSWORD,db=DB,charset=CHARSET):
        # 1. 连接数据库，
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            db=db,
            charset=charset,
            # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
        )
        # ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
        # 2. 创建游标对象，
        self.cur = self.conn.cursor()

    # 3. 对于数据库进行增删改查
    def alter_record(self, sqli):
        ## 1). *********************增删改数据****************************
        try:
            self.cur.execute(sqli)
            self.conn.commit()
        except Exception as e:
            print(sqli+"执行失败:", e)
        else:
            print(sqli+"执行成功;")

    def insert_multi_records(self, insert_sqli,info):
        """

        :param insert_sqli: "insert into hello values(%s, '%s');"
        :param info: info = [(i, "westos%s" %(i)) for i in range(100)]
        :return:
        """
        # 2). *********************插入多条数据****************************
        try:
            # *********************第一种方式********************
            # %s必须手动添加一个字符串， 否则就是一个变量名， 会报错.
            # insert_sqli = "insert into hello values(%d, '%s');"
            # for item in info:
            #     print('insert语句:', insert_sqli % item)
            #     self.cur.execute(insert_sqli % item)

            # *********************第二种方式********************
            # insert_sqli = "insert into hello values(%s, %s);"
            self.cur.executemany(insert_sqli, info)
            self.conn.commit()
        except Exception as e:
            print("插入多条数据失败:", e)
        else:
            # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
            self.conn.rollback()
            print("插入多条数据成功;")

    def select_record(self,sqli):
        # 3). **************************数据库查询*****************************
        result = self.cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
        # print(result)
        # print(self.cur.fetchone())  # 1). 获取下一个查询结果集;
        # print(self.cur.fetchone())
        # print(self.cur.fetchone())
        # print(self.cur.fetchmany(4))  # 2). 获取制定个数个查询结果集；
        info = self.cur.fetchall()  # 3). 获取所有的查询结果
        print(info)
        print(len(info))
        print(self.cur.rowcount)  # 4). 返回执行sql语句影响的行数
        return info

        # #  5). 移动游标指针
        # print(self.cur.fetchmany(3))
        # print("正在移动指针到最开始......")
        # self.cur.scroll(0, 'absolute')
        # print(self.cur.fetchmany(3))
        # print("正在移动指针到倒数第2个......")
        # print(self.cur.fetchall())  # 移动到最后
        # self.cur.scroll(-2, mode='relative')
        # printself.(cur.fetchall())

    def close(self):
        # 4. 关闭游标
        self.cur.close()
        # 5. 关闭连接
        self.conn.close()

    def __del__(self):
        self.close()

if __name__=="__main__":
    connection=MySQLConnection()
    sqli="select * from User;"
    info=connection.select_record(sqli)
    sqli="insert into User(name,vip,gender,age,audioType,speed) values(\"风之子\",2,1,20,1,2);"
    connection.alter_record(sqli)
    # sqli="create table testT(id int,s varchar(10));"
    # connection.alter_record(sqli)
    # sqli="insert into testT(id,s) values(%s,%s);"
    # info=[(1,"好运来"),(2,"向天再借五百年")]
    # connection.insert_multi_records(sqli,info)




