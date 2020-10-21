from flask import Flask,request,render_template,flash,session
import pymysql

pname = None
pchar = None
ploc = None
pphy = None
pcla = None
pord = None
pfam = None
pgen = None
pspe = None


def add_plants(fname):
    # 数据库操作
    i = 1
    # 遍历每条数据
    for line in open(fname,encoding='utf-8'):
        data = eval(line)
        m = list(data['attri'].keys())[-1]
        #获取PlantName Character Location
        pname = data['name']
        if pname == None:
            break
        #pname.replace("\'","\"")
        pchar = data['attri']['2']
        if int(m) < 3:
            ploc = None
        else:
            ploc = data['attri']['3']
        #获取门纲目科属种
        for attr in data['location']:
            attrname = data['location'][attr]
            if '门' in attrname:
                pphy = attrname
            elif '纲' in attrname:
                pcla = attrname
            elif '目' in attrname:
                pord = attrname
            elif '科' in attrname:
                pfam = attrname
            elif '属' in attrname:
                pgen = attrname
            elif '族' in attrname:
                pspe = attrname
            elif '组' in attrname:
                pspe += attrname
            else:
                pass
        print(i,pname)
        #print(i,pname,pchar,pphy,pcla,pord,pfam,pgen,pspe,ploc)
        # 3.执行sql语句
        #sql = "insert into plant values(1,'阿坝蒿','多年生草本。主根细；根状茎细或略粗。','被子植物门 Angiospermae','双子叶植物纲 Dicotyledoneae','桔梗目 Campanulales','菊科 Compositae', '蒿属 Artemisia','艾组 Sect. Artemisia','青海',now())"
        sql = "insert into plant values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"
        row = cursor.execute(sql,(i,pname,pchar,pphy,pcla,pord,pfam,pgen,pspe,ploc))
        i = i+1
        #cursor.execute(sql)
        
        
# 1.数据库连接
conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    db = 'mydb',
    user = 'root',
    password = 'hyy19990907',
    charset = 'utf8'
)
# 2.创建游标对象
cursor = conn.cursor()

filename = 'plant-a.txt'
add_plants(filename)
# 4.提交
conn.commit()
# 5.关闭
conn.close()
# 数据库操作
# 1.数据库连接
'''conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    db = 'mydb',
    user = 'root',
    password = 'hyy19990907',
    charset = 'utf8'
)
# 2.创建游标对象
cursor = conn.cursor()
# 3.sql语句
#sql = "insert into plant values(1,'阿坝蒿','多年生草本。主根细；根状茎细或略粗。','被子植物门 Angiospermae','双子叶植物纲 Dicotyledoneae','桔梗目 Campanulales','菊科 Compositae', '蒿属 Artemisia','艾组 Sect. Artemisia','青海',now())"
sql = "insert into plant values(2,'阿尔泰贝母','叶对生或上部互生，先端不卷曲。','被子植物门 Angiospermae','单子叶植物纲 Monocotyledoneae','百合目 Liliflorae','百合科 Liliaceae','贝母属 Fritillaria', '贝母组 Sect. Fritillaria','新疆',now())"

row = cursor.execute(sql)
# 4.提交
conn.commit()
# 5.关闭
conn.close()'''
