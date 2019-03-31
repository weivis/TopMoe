__author__ = 'Ran'
from app import Flask, cache, login_manager
from ..auth import auth
from flask import render_template, request, redirect, url_for, session
from app.Database import Account
import json
import re
from app import login_manager
from flask_login import login_user, login_required, logout_user, current_user

@login_manager.user_loader
def load_user(id):
    return Account.query.get(int(id))

#登陆
@auth.route('/sign-in', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        jsondata = request.json

        if jsondata['account'] == '':
            return json.dumps({'code':'false', 'text':'账户不能为空'})
        
        if jsondata['password'] == '':
            return json.dumps({'code':'false', 'text':'密码不能为空'})

        account_type = re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", jsondata['account'])
        if(account_type):#邮箱
            account = Account.query.filter_by(useremail=jsondata['account']).first()

        else:#手机
            account = Account.query.filter_by(phone=jsondata['account']).first()

        if (account):
            if account.is_correct_password(str(jsondata['password'])):
                session['key'] = int(account.id)
                session.permanent = True
                login_user(account, remember=True) #jsondata['login_long']
                return json.dumps({'code':1, 'text':'登陆成功'})
            else:
                return json.dumps({'code':0, 'text':'密码错误'})
        else:
            return json.dumps({'code':0, 'text':'账户错误'})

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    if session.get('key'):
    	session.clear()
    else:
    	pass
    return json.dumps({'code':'false', 'text':'成功退出'})