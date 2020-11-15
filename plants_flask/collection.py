from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回

class Collection(object):
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

    # 增加记录前，判断收藏记录是否存在
    def is_collected(self,user_id,plant_id):
        sql = "select * from collection where UserID = "+user_id+" AND PlantID = "+plant_id[0]
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        data = self.cursor.fetchall()
        if len(data) == 1:
            return True
        else:
            return False


    # 增加一条收藏记录
    def add_collection(self,user_id,plant_id):
        flag = self.is_collected(user_id,plant_id)
        # 如果已经收藏过，直接返回
        if flag == True:
            return True
        # 否则，插入收藏记录
        else:
            sql = "select MAX(CollectionID) from collection"
            try:
                self.cursor.execute(sql)             # 执行单条sql语句
                self.conn.commit()                     # 提交到数据库执行
                #return True
            except:
                self.conn.rollback()                   # Rollback in case there is any error
            id_count = self.cursor.fetchall()
            print("收藏记录的id",id_count[0]['MAX(CollectionID)'])
            
            if id_count[0]['MAX(CollectionID)'] == None:
                id_count = 1
            else:
                id_count = id_count[0]['MAX(CollectionID)']
            
            sql = "insert into collection values (%s,%s,%s,now())"
            
            try:
                self.cursor.execute(sql,[str(id_count+1),user_id,plant_id])
                self.conn.commit()                     # 提交到数据库执行
                return True
            except:
                self.conn.rollback()                   # Rollback in case there is any error
                return False

    # 删除一条收藏记录
    def delete_collection(self,user_id,plant_id):
        sql = "delete from collection where PlantID = %s AND UserID = %s"
        try:
            self.cursor.execute(sql,[plant_id,user_id])             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    # 查看收藏记录
    def collection_list(self,user_id):
        sql = "select * from collection,plant where UserID = %s AND collection.PlantID = plant.PlantID"
        try:
            self.cursor.execute(sql,[user_id])             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            resdata = []
            for temp in self.cursor.fetchall(): # 所有结果
                print(temp)
                resdata.append(temp)
            return resdata # 以数组形式返回
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False