
from flask import Flask,jsonify,request,json
from users import User
from plant import Plant
from collection import Collection
import re

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

# 1.直接执行这个文件，那么__name__ = __main__
# 2.__name__ = 当前文件的名字

app = Flask(__name__) # 声明Flask类的变量
app.config['JSON_AS_ASCII'] = False

# 判断合法字符
def is_string_validate(str):
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",str)
    if len(str) == len(sub_str):
        # 说明合法
        return False
    else:
        # 不合法
        return True


#########用户类接口函数#########

# 用户登录
@app.route('/dologin',methods=['POST'])
def dologin():
    # post方法
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        name = get_data['uname']
        pwd = get_data['upwd']
        print("姓名：", name, '密码：', pwd)
        u = User()
        data = u.user_sign_in(name, pwd)# 这里是在用户和管理员两个表查询，后面要改一下
        if data != None:
            resData = {
                "resCode" : 0,
                "data" : data,
                "message" : '登录成功'
                #回去之后应该时跳转到首页，就是home.vue
            }
            return jsonify(resData)
        else:
            resData = {
                "resCode" : 1,
                "data" : data,
                "message" : '用户名或密码不正确'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 查看用户信息
@app.route('/userinfo',methods=['POST','GET']) # 路由
def get_user_by_userid():
    if request.method == 'POST':
        get_data = json.loads(request.get_data(as_text=True))
        user_id = get_data['userID']
        print("user_id = ",user_id)
        u = User()
        data = u.get_one_user(user_id)
        print(data)
        resData = {
            'resCode' : 0,
            'data' : data,
            'massage' : '得到用户信息'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 用户注册（针对普通用户的注册功能，管理员账号是数据库操作人员给的）
# 用户信息（昵称，密码）
@app.route('/userloginup',methods=['POST']) # 路由
def add_user():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        param = {
            'name' : get_data['u_login_up_name'],
            'pwd' : get_data['u_login_up_pwd']
        }
        #初始化
        u = User()
        #不合法输入怎么办？
        for i in param:
            if is_string_validate(param[i]):
                resData = {
                    "resCode": 1, # 非0即错误 1
                    "data": [],# 数据位置，一般为数组
                    "message": '参数错误'
                }
                return jsonify(resData)
        #u.login_up()函数还没写哦
        data = u.login_up(param)
        print('param = ',param)
        if data == False:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '注册失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : [],
            "message" : '注册成功'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


# 用户修改自己的信息（需要传递用户ID和新的昵称）
# 修改用户信息（实质上就是修改用户名，这里要注意无意义字符的判断，规定好用户名的格式和长度）
# 管理员不能修改用户信息~
# （用户ID和新用户名）
@app.route('/<int:user_id>/modify_userinfo',methods=['GET','POST']) # 路由
def modify_userinfo(user_id):
    if request.method == 'POST':
        #获取参数
        print('捕获到post请求：',user_id,' 修改昵称')
        get_data = json.loads(request.get_data(as_text=True))
        param = {
            'new_name' : get_data['new_name']
        }
        #不合法输入怎么办？
        if is_string_validate(param['new_name']):
            resData = {
                "resCode": 1, # 非0即错误 1
                "data": [],
                "message": '昵称不符合要求，请重新输入'
            }
            return jsonify(resData)
        #初始化
        u = User()
        data = u.modify_userinfo(user_id,param)
        if data == True:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '成功修改信息'
            }
            # 注意这个地方，要刷新用户个人资料页面，在script里面，判断更新成功就刷新页面
            return jsonify(resData)
        else:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '修改信息失败'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


# 修改密码（用户ID和用户密码，新密码？？？？这里再想一下）
# 用户ID和旧密码，新密码（提交前，在script里判断输入的两次密码是否相同，如何实现百度一下）
@app.route('/<int:user_id>/modify_pwd',methods=['GET','POST'])
def modify_passwd(user_id):
    if request.method == 'POST':
        #获取参数
        print('捕获到post请求：',user_id,' 修改密码')
        get_data = json.loads(request.get_data(as_text=True))
        param = {
            'new_pwd' : get_data['new_pwd']
        }
        #不合法输入怎么办？
        if is_string_validate(param['new_pwd']):
            resData = {
                "resCode": 1, # 非0即错误 1
                "data": [],
                "message": '密码不符合要求，请重新输入'
            }
            return jsonify(resData)
        #初始化
        u = User()
        data = u.modify_passwd(user_id,param)
        if data == True:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '成功修改密码'
            }
            return jsonify(resData)
        else:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '修改密码失败'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


# 删除用户信息（管理员可以删除用户信息）
@app.route('/<int:user_id>/delete_user',methods=['GET','POST'])
def delete_user(user_id):
    if request.method == 'POST':
        u = User()
        data = u.delete_user(user_id)
        if data == True:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '已删除该用户'
            }
            # 这里要刷新管理员的管理页面
            return jsonify(resData)
        else:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '删除失败'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


#########植物类接口函数#########

# 根据植物ID查询植物数据并返回（植物ID）
@app.route('/plant/<int:plantID>',methods=['POST']) # 路由
def get_plant_by_id(plantID):
    if request.method == 'POST':
        print('捕获到post请求：',plantID)
        #plant_cate就是植物标签,这里是双子叶
        #如何根据标签确定查询语句的范围哦？
        # 捕获到post请求：从而确定查询什么数据，在这里要完成查询并返回数据
        p = Plant()
        data = p.get_plant_by_plantID(plantID)
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

# 根据标签，查询数据并返回（植物标签）
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

# 搜索功能，查询数据并返回（用户输入关键字）
@app.route('/search',methods=['POST']) # 路由
def get_plant_by_search():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        key = get_data['key']
        p = Plant()
        #不合法输入怎么办？
        if is_string_validate(key):
            resData = {
                "resCode": 1, # 非0即错误 1
                "data": [],# 数据位置，一般为数组
                "message": '参数错误'
            }
            return jsonify(resData)
        data = p.get_plant_by_search(key)
        #key是提交的关键字，用于数据库查询即可
        print('key = ',key)
        if len(data) == 0:
            resData = {
                "resCode" : 0,            
                "data" : data,
                "message" : '数据为空'
            }
            return jsonify(resData)
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

# 增加一条植物信息（待添加的植物信息）
@app.route('/createplant',methods=['POST']) # 路由
def add_plant():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        param = {
            'Pname' : get_data['pname'],
            'Pchar' : get_data['pchar'],
            'Pphy'  : get_data['pphy'],
            'Pcla' : get_data['pphy'],
            'Pord' : get_data['pphy'],
            'Pfam' : get_data['pphy'],
            'Pgen' : get_data['pphy'],
            'Pspe' : get_data['pphy'],
            'Ploc' : get_data['ploc']
        }
        #初始化
        p = Plant()
        #不合法输入怎么办？
        for i in param:
            if is_string_validate(param[i]):
                resData = {
                    "resCode": 1, # 非0即错误 1
                    "data": [],# 数据位置，一般为数组
                    "message": '参数错误'
                }
                return jsonify(resData)
        data = p.add_plant(param)
        print('param = ',param)
        if data == False:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '添加植物信息失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : [],
            "message" : '已添加该植物信息'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 修改植物信息（所有植物信息）
@app.route('/<int:plant_id>/modify_plantinfo',methods=['GET','POST'])
def modify_plantinfo(plant_id):
    if request.method == 'POST':
        print('捕获到post请求：植物',plant_id,' 修改信息')
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        param = {
            'Pname' : get_data['pname'],
            'Pchar' : get_data['pchar'],
            'Pphy'  : get_data['pphy'],
            'Pcla' : get_data['pphy'],
            'Pord' : get_data['pphy'],
            'Pfam' : get_data['pphy'],
            'Pgen' : get_data['pphy'],
            'Pspe' : get_data['pphy'],
            'Ploc' : get_data['ploc']
        }
        #不合法输入
        for i in param:
            if is_string_validate(param[i]):
                resData = {
                    "resCode": 1, # 非0即错误 1
                    "data": [],# 数据位置，一般为数组
                    "message": '参数错误'
                }
                return jsonify(resData)
        #初始化
        p = Plant()    
        data = p.delete_plant_by_plantID(plant_id)
        if data == True:
            data = p.add_plant_after_delete(plant_id,param)
            print('param = ',param)
            if data == False:
                resData = {
                    "resCode" : 0,            
                    "data" : [],
                    "message" : '修改植物信息失败'
                }
                return jsonify(resData)
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '已修改该植物信息'
            }
            return jsonify(resData)
        else:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '修改植物信息失败'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 删除植物信息（管理员可以删除植物信息）
@app.route('/<int:plant_id>/delete_plant',methods=['GET','POST'])
def delete_plant(plant_id):
    if request.method == 'POST':
        p = Plant()
        data = p.delete_plant_by_plantID(plant_id)
        if data == True:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '已删除该植物'
            }
            # 这里要刷新管理员的管理页面
            return jsonify(resData)
        else:
            resData = {
                "resCode" : 1,            
                "data" : [],
                "message" : '删除失败'
            }
            return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


#########收藏类接口函数#########
# UserID如何作为全局变量

# 收藏某个植物（用户ID，植物ID）
# 更细致一点，要看是不是已经收藏过这个植物了（代码还要修改）
@app.route('/addcollect',methods=['GET','POST'])
def collect():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        user_id = get_data['u_id']
        plant_id = get_data['p_id']
        c = Collection()
        data = c.add_collection(user_id,plant_id)
        if data == False:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '收藏失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : [],
            "message" : '已收藏该植物'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


# 删除收藏（用户ID，植物ID）
@app.route('/deletecollect',methods=['GET','POST'])
def delete_collect():
    if request.method == 'POST':
        #获取参数
        get_data = json.loads(request.get_data(as_text=True))
        user_id = get_data['u_id']
        plant_id = get_data['p_id']
        c = Collection()
        data = c.delete_collection(user_id,plant_id)
        if data == False:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '取消收藏失败'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : [],
            "message" : '已取消收藏'
        }
        # 这里要刷新收藏页面
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)

# 用户查看自己的收藏（用户ID)
@app.route('/<int:user_id>/collection_list',methods=['GET','POST'])
def collectlist(user_id):
    if request.method == 'POST':
        #获取参数
        c = Collection()
        data = c.collection_list(user_id)
        if len(data) == 0:
            resData = {
                "resCode" : 0,            
                "data" : [],
                "message" : '收藏为空'
            }
            return jsonify(resData)
        resData = {
            "resCode" : 0,            
            "data" : data,
            "message" : '得到收藏列表'
        }
        return jsonify(resData)
    else:
        resData = {
            "resCode" : 1,            
            "data" : [],
            "message" : '请求方式错误'
        }
        return jsonify(resData)


if __name__ == '__main__': # 如果是直接执行文件，那么就执行下面的代码
    app.run(host = '127.0.0.1', port = 1943, debug = True)