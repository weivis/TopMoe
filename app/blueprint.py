from app import app
from app.index import index
from app.login import login
from app.register import register

'''
    设置访问后缀
    url_prefix='/watch'
'''

# 默认域名
# app.config['SERVER_NAME'] = 'topmoe.com'
# , subdomain='www'

# 注册蓝图
app.register_blueprint(index)

# 系统api登录注册路由
app.register_blueprint(login, url_prefix='/api/sgin-in')
app.register_blueprint(register, url_prefix='/api/register')