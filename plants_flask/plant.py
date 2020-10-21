from pymysql import connect
from flask import Flask,request,render_template,flash,session
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
    

    def get_cates_plants_30(self, plant_cate):
        # 这个sql语句还没写好哦，没有考虑植物的类型
        print('plant_cate = ',plant_cate)
        cate = None
        if '门' in plant_cate:
            cate = "Phylum"
        elif '纲' in plant_cate:
            cate = "Class"
        elif '目' in plant_cate:
            cate = "Order"
        elif '科' in plant_cate:
            cate = "Family"
        elif '属' in plant_cate:
            cate = "Genus"
        elif '族' in plant_cate:
            cate = "Specice"
        elif '组' in plant_cate:
            cate = "Specice"
        else:
            pass
        sql = "select * from plant limit 4"
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall(): # 所有结果
            print(temp)
            data.append(temp)
        return data # 以数组形式返回