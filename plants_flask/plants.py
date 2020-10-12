from pymysql import connect
from pymysql.cursors import DictCursor # 得到字典形式的返回

class Plant(object):
    def __init__(self): # 创建对象同时要执行的代码
        self.conn = connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'hyy19990907',
            database = 'mydb',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor(DictCursor) # 可以返回字典形式

    def __del__(self): # 释放对象同时要执行的代码
        self.cursor.close()
        self.conn.close()
    
    def get_one_user(self):
        sql = 'select * from ordinaryuser limit 1'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall(): # 所有结果
            print(temp)
            data.append(temp)
        return data # 以数组形式返回