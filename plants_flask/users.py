from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回

class User(object):
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
    
    #用户注册
    def login_up(self,item):
        sql = "select MAX(UserID) from ordinaryuser"
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            #return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        id_count = self.cursor.fetchall()
        print("用户数量 = ",id_count[0]['MAX(UserID)'])

        print(item['name'],item['pwd'])
        sql = "insert into ordinaryuser values ("+str(id_count[0]['MAX(UserID)']+1)+",'"+item['name']+"','"+item['pwd']+"',now(),'u',0)"
        #self.cursor.execute(sql,[item['name'],item['pwd']])
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    #登录处理
    def user_sign_in(self,u_name,u_pwd):
        # 3.sql语句
        sql = "select * from ordinaryuser where UserName = %s and UserPassword = %s"
        self.cursor.execute(sql,[u_name,u_pwd])
        # 4.处理结果，查询单条数据，无需提交
        rs = self.cursor.fetchone()
        print(rs)

        # 用户名和密码不正确
        return rs

    #修改用户信息
    def modify_userinfo(self,user_id,param):
        sql = "update ordinaryuser set UserName = '"+param['new_name']+"' where UserID = '"+user_id+"'"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        return False

    #修改密码
    def modify_passwd(self,user_id,param):
        sql = "update ordinaryuser set UserPassword = '"+param['new_pwd']+"' where UserID = '"+user_id+"'"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        return False

    #获得一个用户的个人资料
    def get_one_user(self,user_id):
        sql = "select * from ordinaryuser where UserID = "+str(user_id)
        print(sql)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall(): # 所有结果
            print(temp)
            data.append(temp)
        return data # 以数组形式返回

    def delete_user(self,user_id):
        sql = "delete from ordinaryuser where UserID = '"+user_id+"'"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        return False