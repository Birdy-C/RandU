#-*- coding:utf-8 -*-
# models.py

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from datetime import datetime


import os
import uuid
import app



class User(UserMixin, app.db.Model):
    __tablename__ = 'users'
    id = app.db.Column(app.db.Integer, primary_key=True)
    email = app.db.Column(app.db.String(64), unique=True, index=True)
    username = app.db.Column(app.db.String(64))
    #power = app.db.Column(app.db.Integer, app.db.ForeignKey('roles.id'))
    password_hash = app.db.Column(app.db.String(128))
    confirmed = app.db.Column(app.db.Boolean, default=False)

    
    country=app.db.Column(app.db.String(64))#国家
    province=app.db.Column(app.db.String(64))#省份
    city=app.db.Column(app.db.String(64))#城市
    moreaddress=app.db.Column(app.db.String(64))#详细地址
    power=app.db.Column(app.db.Integer)#用户权限：0超级管理员，1管理员，2普通用户
    introduction=app.db.Column(app.db.String(100))#个人介绍
    gender = app.db.Column(app.db.Integer)#性别：0男，1女


    posts=app.db.relationship('Post',backref='author',lazy='dynamic')


    def __init__(self, email):
        self.email = email
        self.id = self.get_id()



    """这个暂时应该没啥用，除非做测试"""
    def get_password_hash(self):

        """try to get password hash from file.

        :return password_hash: if the there is corresponding user in
                the file, return password hash.
                None: if there is no corresponding user, return None.
        """
        try:
            with open(PROFILE_FILE) as f:
                user_profiles = json.load(f)
                user_info = user_profiles.get(self.username, None)
                if user_info is not None:
                    return user_info[0]
        except IOError:
            return None
        except ValueError:
            return None
        return None
    


    """下面俩函数用于记住用户的登录状态"""
    def get_id(self):
        """get user id from profile file, if not exist, it will
        generate a uuid for the user.
                        pass
        """
        if self.username is not None:
            print self.id
            return unicode(self.id)

    @staticmethod
    def get(user_id):
        """try to return user_id corresponding User object.
        This method is used by load_user callback function
        """
        return self.id
       
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')


    # 下面一串是密码吧大概

    @password.setter
    def password(self, password):
        self.password_hash = password
        #self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        print self.password_hash
        print password
        return self.password_hash == password
        #return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = 1
        app.db.session.add(self)
        app.db.session.commit()
        return True

    def __repr__(self):
        return '<User %r>' % self.username




class Letter(app.db.Model):#信表
    __tablename__='letters'
    id = app.db.Column(app.db.Integer, primary_key=True)#信ID
    addfrom=app.db.Column(app.db.String(64))#寄信方
    addto=app.db.Column(app.db.String(64))#收信方
    nowstate=app.db.Column(app.db.Integer)#信的状态：0在路上，1已到达
    def __repr__(self):
        return '<User %r>' % self.id

class Post(app.db.Model):
    __tablename__='posts'
    id=app.db.Column(app.db.Integer,primary_key=True)
    body=app.db.Column(app.db.Text)#动态内容本体
    timestamp=app.db.Column(app.db.DateTime,index=True,default=datetime.utcnow)
    author_id=app.db.Column(app.db.Integer,app.db.ForeignKey('users.id'))