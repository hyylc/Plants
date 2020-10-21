#获取所有植物的标签，导入数据库
from flask import Flask,request,render_template,flash,session
import pymysql
import random
ch = ['a','b','c','d','e','f','g','h','j','k','l','m','n','o','p','q','r','s','t','w']
phy = []
cla = []
order = []
fam = []
gen = []
spe = []
#读取所有文件，dict格式，从中读取

def attrappend(str,lis):
    if str not in lis:
        lis.append(str)

def write_to_file():
    fp = open('cate_phy.txt','a',encoding='utf-8')
    fp.write(str(phy))
    fp.close()
    fp = open('cate_cla.txt','a',encoding='utf-8')
    fp.write(str(cla))
    fp.close()
    fp = open('cate_order.txt','a',encoding='utf-8')
    fp.write(str(order))
    fp.close()
    fp = open('cate_fam.txt','a',encoding='utf-8')
    fp.write(str(fam))
    fp.close()
    fp = open('cate_gen.txt','a',encoding='utf-8')
    fp.write(str(gen))
    fp.close()
    fp = open('cate_spe.txt','a',encoding='utf-8')
    fp.write(str(spe))
    fp.close()



def Get_cates(fname):
    for line in open(fname,encoding='utf-8'):
        data = eval(line)
        for attr in data['location']:
            attrname = data['location'][attr]
            if '门' in attrname:
                attrappend(attrname,phy)
            elif '纲' in attrname:
                attrappend(attrname,cla)
            elif '目' in attrname:
                attrappend(attrname,order)
            elif '科' in attrname:
                attrappend(attrname,fam)
            elif '属' in attrname:
                attrappend(attrname,gen)
            elif '族' in attrname:
                attrappend(attrname,spe)
            elif '组' in attrname:
                attrappend(attrname,spe)
            else:
                pass


Get_cates('plant-a.txt')
print(phy)
write_to_file()
'''print(len(ch))
for i in ch:
    filename = 'plant-'+i+'.txt'
    print(filename)
    Get_cates(filename)
print(phy)'''


'''# 数据库操作
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
# 3.sql语句
#sql = "insert into plant values(1,'阿坝蒿','多年生草本。主根细；根状茎细或略粗。','被子植物门 Angiospermae','双子叶植物纲 Dicotyledoneae','桔梗目 Campanulales','菊科 Compositae', '蒿属 Artemisia','艾组 Sect. Artemisia','青海',now())"
sql = "insert into plant values(2,'阿尔泰贝母','叶对生或上部互生，先端不卷曲。','被子植物门 Angiospermae','单子叶植物纲 Monocotyledoneae','百合目 Liliflorae','百合科 Liliaceae','贝母属 Fritillaria', '贝母组 Sect. Fritillaria','新疆',now())"

row = cursor.execute(sql)
# 4.提交
conn.commit()
# 5.关闭
conn.close()'''
