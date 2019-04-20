__author__ = 'Ran'
from app import Flask, cache
from ..login import login
from flask import render_template, request, session, redirect

from app.DB_Account import Account

from flask_login import login_user, login_required, logout_user, current_user

import json
import re

# 登录api /sgin-in/api
@login.route('/', methods=["GET", "POST"])
def loginAccount():
    '''
        {"account":"", "password":""}
    '''

    # 判断是否登录状态
    if current_user.is_authenticated:
        return json.dumps({'code': 0, 'text': '你已登录过'})

    else:
        if request.method == 'POST':

            # 获取json数据
            jsondata = request.json
            print(jsondata)

            # 判断用户输入的内容是否为空
            if jsondata['phone'] == '':
                return json.dumps({'code': 0, 'text': '账户不能为空'})

            elif jsondata['password'] == '':
                return json.dumps({'code': 0, 'text': '密码不能为空'})

            else:
                # 判断传入account 是属于手机号 还是 邮箱
                account = Account.query.filter_by(userphone=jsondata['phone']).first()

                if (account):  # 判断账户是否存在
                    # 判断json的密码和根据account获取到的用户密码是否一致
                    if account.is_correct_password(str(jsondata['password'])):
                        session.permanent = True
                        login_user(account, remember=True)
                        return json.dumps({'code': 1, "userid": account.id, 'text': '登陆成功'})
                    else:
                        return json.dumps({'code': 0, 'text': '账户或密码错误'})
                else:
                    return json.dumps({'code': 0, 'text': '账户不存在'})
        else:
            return '登录页面'
