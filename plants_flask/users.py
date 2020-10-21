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
    
    #登录处理
    def user_sign_in(self,u_name,u_pwd):
        # 3.sql语句
        sql = "select * from ordinaryuser where UserName = %s and UserPassword = %s"
        self.cursor.execute(sql,[u_name,u_pwd])
        # 4.处理结果，查询单条数据，无需提交
        rs = self.cursor.fetchone()
        print(rs)
        # 5.关闭
        self.conn.close()

        # 用户名和密码不正确
        if rs == None:
            flash('登录失败，用户名或者密码不正确')
            return render_template('login.html')
        else:
            # 设置会话
            session['name'] = u_name
            # 获取会话中的值 session['name']
            return render_template('index.html',name = u_name)


    def get_one_user(self):
        sql = 'select * from ordinaryuser limit 1'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall(): # 所有结果
            print(temp)
            data.append(temp)
        return data # 以数组形式返回