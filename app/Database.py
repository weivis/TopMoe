# -*- coding: utf-8 -*-
from app import db
from flask_login import UserMixin, current_user
from flask_bcrypt import check_password_hash, generate_password_hash

# 账户表
class Account(db.Model, UserMixin):

    # 表的名字
    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True) #用户名不能重复
    password = db.Column(db.String(100))
    userhead = db.Column(db.String(255))
    useremail = db.Column(db.String(150), unique=True) #用户邮箱不能重复
    phone = db.Column(db.String(100), unique=True) #用户手机不能重复
    userintroduce = db.Column(db.Text) #个人介绍
    article_count = db.Column(db.Integer) #文章数量统计
    reply_count = db.Column(db.Integer) #回复数量统计
    follow_count = db.Column(db.Integer) #关注数量统计
    fans_count = db.Column(db.Integer) #粉丝数量统计

    # 定义对象
    def __init__(self, username=None, password=None, userhead=None, useremail=None, userphone=None, userintroduce=None, article_count=0, reply_count=0, follow_count=0, fans_count=0):
        self.username = username
        self.password = generate_password_hash(password)
        self.userhead = userhead
        self.useremail = useremail
        self.userphone = userphone
        self.userintroduce = userintroduce
        self.article_count = article_count
        self.reply_count = reply_count
        self.follow_count = follow_count
        self.fans_count = fans_count
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