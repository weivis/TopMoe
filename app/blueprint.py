from app import app, Flask
from app.auth import auth
from app.register import register

app.config['SERVER_NAME'] = 'topmoe.com'
app.register_blueprint(auth, subdomain='www', url_prefix='/login-auth')
'''
/login-auth
    /sign-in #登录
    /logout  #退出
'''

app.register_blueprint(register, subdomain='www', url_prefix='/register')
'''
/register
    /create
'''