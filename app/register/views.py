__author__ = 'Ran'
from app import Flask, db
from ..register import register
from flask import render_template, request, session, redirect
from flask_login import current_user

from app.DB_Account import Account

import json
#首页
@register.route('/api', methods=["GET", "POST"])
def registerAccount():

    '''
        {"username":"", "password":"", "userphone":"", "useremail":""}
    '''

    if current_user.is_authenticated:
        return json.dumps({'code': 0, 'text': '你已登录过'})

    else:
        if request.method == 'POST':
            jsondata = request.json
            print(jsondata)

            if jsondata['username'] == '':
                return json.dumps({'code':0, 'text':'用户名不能为空'})

                '''
                elif jsondata['useremail'] == '':
                    return json.dumps({'code':0, 'text':'邮箱不能为空'})

                elif Account.query.filter_by(useremail = jsondata['useremail']).first():
                    return json.dumps({'code':0, 'text':'该邮箱以注册过'})
                '''

            elif jsondata['userphone'] == '':
                return json.dumps({'code':0, 'text':'手机不能为空'})

            elif jsondata['password'] == '':
                return json.dumps({'code':0, 'text':'密码不能为空'})

            elif Account.query.filter_by(username = jsondata['username']).first():
                return json.dumps({'code':0, 'text':'用户名已存在'})

            elif Account.query.filter_by(userphone = jsondata['userphone']).first():
                return json.dumps({'code':0, 'text':'该手机已经注册过'})

            else:
                Account(username=jsondata['username'], userphone = jsondata['userphone'], password = str(jsondata['password']))#, useremail = jsondata['useremail']
                return json.dumps({'code':1, 'text':'注册成功'})

        else:
            return json.dumps({'code':0, 'text':'非法访问'})