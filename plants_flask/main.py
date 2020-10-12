
from flask import Flask,jsonify
from plants import Plant


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
    plant = Plant()
    data = plant.get_one_user()
    return jsonify(data)

if __name__ == '__main__': # 如果是直接执行文件，那么就执行下面的代码
    app.run(host = '127.0.0.1', port = 1943, debug = True)