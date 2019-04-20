# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin, current_user
from flask_bcrypt import check_password_hash, generate_password_hash

# 账户表
class Account(db.Model, UserMixin):

    '''
        username, password, userhead, useremail, userphone
        注册用户调用Account(传入__init__指定参数 通过处理后进入self类进行提交)
        Account(username, phone, password, user_email)
        调用添加和关闭连接
        db.session.add(generate_newuserdata)
        db.session.commit()

        调用这个方法判断密码是否正确
        使用前需要先获取account对象
        account = Account.query.filter_by(查询用户方法).first()
        然后在调用
        account.is_correct_password(传入密码)
    '''

    # 表的名字
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True) #用户名不能重复
    password = db.Column(db.String(100))
    userhead = db.Column(db.String(255))
    #useremail = db.Column(db.String(150), unique=True) #用户邮箱不能重复
    userphone = db.Column(db.String(100), unique=True) #用户手机不能重复

    # 定义对象
    def __init__(self, username=None, password=None, userhead=None, userphone=None, #useremail=None,
        #在此处添加需要追加的字段
        ):

        self.username = username
        self.password = generate_password_hash(password)
        self.userphone = userphone
        self.userhead = userhead
        #self.useremail = useremail

        '''
            在此处添加需要追加的字段
        '''

        self.update()  # 提交数据

    def __repr__(self):
        return '<User %r>' % self.username

    #密码检验
    def is_correct_password(self, plaintext):
        if check_password_hash(self.password, plaintext):
            return True

    # 提交数据函数
    def update(self):
        db.session.add(self)
        db.session.commit()

#db.create_all()