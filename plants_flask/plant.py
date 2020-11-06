from pymysql import connect
from flask import Flask,request,render_template,flash,session
from pymysql.cursors import DictCursor # 得到字典形式的返回

class Plant(object):
    # 创建对象同时要执行的代码
    def __init__(self): 
        self.conn = connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'root',
            password = 'hyy19990907',
            database = 'mydb',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor(DictCursor) # 可以返回字典形式

    # 释放对象同时要执行的代码
    def __del__(self): 
        self.cursor.close()
        self.conn.close()
    
    # 删除植物
    def delete_plant_by_plantID(self,plantID):
        sql = "delete from plant where PlantID = "+str(plantID)
        print("sql = ",sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    # 添加一条植物信息
    def add_plant(self,item):
        # 当前id最大值
        sql = "select MAX(PlantID) from plant"
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            #return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        id_count = self.cursor.fetchall()
        sql = "insert into plant values("+str(id_count[0]['MAX(PlantID)']+1)+",'"+item['Pname']+"','"+item['Pchar']+"','"+item['Pphy']+"','"+item['Pcla']+"','"+item['Pord']+"','"+item['Pfam']+"','"+item['Pgen']+"','"+item['Pspe']+"','"+item['Ploc']+"',now())"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    # 删除后添加
    def add_plant_after_delete(self,plant_id,item):
        sql = "insert into plant values("+str(plant_id)+",'"+item['Pname']+"','"+item['Pchar']+"','"+item['Pphy']+"','"+item['Pcla']+"','"+item['Pord']+"','"+item['Pfam']+"','"+item['Pgen']+"','"+item['Pspe']+"','"+item['Ploc']+"',now())"
        print(sql)
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    # 修改一条植物信息
    def modify_plant(self,id,item):
        # 当前id最大值
        sql = "select PlantID from plant where"
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            #return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
        id_count = self.cursor.fetchall()
        
        sql = "insert into plant values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,[id_count+1,item['Pname'],item['Pchar'],item['Pphy'],item['Pcla'],item['Pord'],item['Pfam'],item['Pgen'],item['Pspe'],item['Ploc']])
        try:
            self.cursor.execute(sql)             # 执行单条sql语句
            self.conn.commit()                     # 提交到数据库执行
            return True
        except:
            self.conn.rollback()                   # Rollback in case there is any error
            return False

    # 点击植物，获取某个植物的信息
    def get_plant_by_plantID(self,plantID):
        sql = "select * from plant where plant.PlantID = "+str(plantID)
        print("sql = ",sql)
        self.cursor.execute(sql)
        resdata = []
        for temp in self.cursor.fetchall(): # 所有结果
            print(temp)
            resdata.append(temp)
        return resdata # 以数组形式返回

    # 关键字搜索植物
    def get_plant_by_search(self,key):
        sql = "select * from plant where PlantName like '%"+key+"%' limit 30"
        print("sql = ",sql)
        self.cursor.execute(sql)
        resdata = []
        for temp in self.cursor.fetchall(): # 所有结果
            print(temp)
            resdata.append(temp)
        return resdata # 以数组形式返回

    def get_all_plants(self):
        sql = "select * from plant"
        self.cursor.execute(sql)
        resdata = []
        for temp in self.cursor.fetchall(): # 所有结果
            print(temp)
            resdata.append(temp)
        return resdata # 以数组形式返回
        
    # 根据标签，返回30条植物信息
    def get_cates_plants_30(self, plant_cate):
        # 这里要判断，英文对应的中文标签，确定查询的cate是啥
        select_cate = plant_cate
        cate_type = ['phy','cla','order','fam','gen','spe']
        for i in cate_type:
            for line in open('cate_'+i+'.txt',encoding='utf-8'):
                    if plant_cate in line:
                        plant_cate = line
        print('plant_cate = ',plant_cate)
        cate = ""
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
        print("cate = ",cate)
        sql = "select PlantID,PlantName,Characters,Location from plant where plant."+cate+" like '%"+select_cate+"%' limit 30"
        print("sql = ",sql)
        self.cursor.execute(sql)
        resdata = []
        for temp in self.cursor.fetchall(): # 所有结果
            print(temp)
            resdata.append(temp)
        return resdata # 以数组形式返回