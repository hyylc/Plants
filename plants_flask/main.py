
from flask import Flask,jsonify,request,json
from users import User
from plant import Plant

"""
接口说明：
1.返回的是json数据
2.结构如下
{
    resCode:0 # 非0为错误
    data: #数据位置，一般为数组
    message: '对本次请求的说明'
}
"""


app = Flask(__name__) # 声明Flask类的变量

# 1.直接执行这个文件，那么__name__ = __main__
# 2.__name__ = 当前文件的名字
app.config['JSON_AS_ASCII'] = False

@app.route('/') # 路由
def hello_world():
    u = User()
    data = u.get_one_user()
    return jsonify(data)

@app.route('/plants_header') # 路由
def get_header():
    # 注意返回数据的格式
    resData = {
        "resCode" : 0,
        "data" : [
            {'id':0,'name':'首页','url':'/shouye'},
            {'id':1,'name':'个人中心','url':'/userinfo'}
        ],
        "message" : '数据'
    }
    return jsonify(resData)

# 根据查询标签，查询数据并返回
@app.route('/<string:plant_cate>',methods=['POST']) # 路由
def get_cate_infos(plant_cate):
    #这里还要写plant类的函数，但是还没有写~~~哭泣
    if request.method == 'POST':
        print('捕获到post请求：',plant_cate)#plant_cate就是植物标签,这里是双子叶
        #如何根据标签确定查询语句的范围哦？
        # 捕获到post请求：从而确定查询什么数据，在这里要完成查询并返回数据
        p = Plant()
        data = p.get_cates_plants_30(plant_cate)
        resData = {
            "resCode" : 0,            
            "data" : data,
            "message" : '得到植物信息'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 返回当前用户信息，需要查询指定用户的信息，待修改
@app.route('/userinfo',methods=['GET','POST']) # 路由
def get_userinfo():
    u = User()
    data = u.get_one_user()
    resData = {
        "resCode" : 0,            
        "data" : data,
        "message" : '得到用户信息'
    }
    return jsonify(resData)

if __name__ == '__main__': # 如果是直接执行文件，那么就执行下面的代码
    app.run(host = '127.0.0.1', port = 1943, debug = True)