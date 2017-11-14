#-*- coding:utf-8 -*-
"""
Routes and views for the flask application.
"""

import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')
from datetime import datetime

from flask import Flask,url_for,render_template,request,url_for,redirect,send_from_directory
from flask import render_template, flash 
from flask import current_app

from flask_moment import Moment
from flask_wtf.csrf import CSRFProtect
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand

from flask_mail import Mail, Message
from threading import Thread

# from models import User
from flask_login import login_user, login_required,logout_user
from flask_login import LoginManager, current_user

# from models import User,Letter,Userinfo
import forms
import models

app = Flask(__name__)
app.config['FLASKY_POSTS_PER_PAGE']=10
# for database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'data.sqlite')

print 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True
db = SQLAlchemy(app)
manager=Manager(app)
migrate=Migrate(app,db) #配置迁移
manager.add_command("db",MigrateCommand) #配置迁移命令

# for encryption
csrf = CSRFProtect()
csrf.init_app(app)


# use login manager to manage session
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'
login_manager.init_app(app=app)


# 这个callback函数用于reload User object，根据session中存储的user id
@login_manager.user_loader
def load_user(user_id):
    return  models.User.query.filter_by(id = user_id).first()

#下面是SMTP服务器配置
app.config['MAIL_SERVER'] = 'smtp.163.com' #电子邮件服务器的主机名或IP地址
app.config['MAIL_PORT'] = 25 #电子邮件服务器的端口
app.config['MAIL_USE_TLS'] = True #启用传输层安全
app.config['MAIL_USERNAME'] = 'randu_group@163.com'
app.config['MAIL_PASSWORD'] = 'ZJU517'
app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[@RandU]'
app.config['FLASKY_MAIL_SENDER'] = 'RandU Group <randu_group@163.com>'
mail = Mail(app)

#app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
#app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
@app.route('/',methods=['GET','POST'])
@app.route('/login',methods=['GET','POST'])
def login():
    """Renders the home page."""
    info = ''
    form = forms.LoginForm()
    # print form.email.data
    # print request.form.get('email', None)
    if form.validate_on_submit():
        user_name = request.form.get('email', None)
        password = request.form.get('password', None)
        remember_me = request.form.get('remember_me', False)
        # print user_name,password
        user = models.User.query.filter_by(email = user_name).first()
        if user is None:
            flash('辣鸡你不在表里')
        elif form.password is None:
            flash('您填个密码呀')
        elif user.verify_password(form.password.data):

            # print 'login_in_user'
            login_user(user, form.remember_me.data)
            #ok = login_user(user, form.remember_me.data)
            # print ok

            flash('没想到吧居然登录成功了')
            return redirect(request.args.get('next') or url_for('user'))
        else:
            print user.password_hash
            flash('记错密码惹.')
    else:
        if request.form.get('email', None) is None:
            flash('Please Enter Accuate Email')
        if request.form.get('password', None) is None:
            flash('Please Enter Password')

    return render_template(
        'index.html',
        title='Home',
		info=info,
        year=datetime.now().year,
        form=form,
    )



@app.route('/register', methods=['GET', 'POST'])
def register():
    global db
    form = forms.RegistrationForm()
    """Renders the register page."""

    print request.form.get('username',None)
    email_test =  request.form.get('email',None)
    print request.form.get('password',None)
    print request.form.get('password2',None)
    print request.form.get('gender',None)
    print request.form.get('country',None)
    print request.form.get('city',None)
    print request.form.get('moreaddress',None)
    print form.validate_on_submit()

    user = models.User.query.filter_by(email = email_test).first()
    if user is not None:
        flash('您仿佛已经注册过了')
    elif request.form.get('country','') == '国家':
        flash('please enter the country.')
    elif request.form.get('province','') == '省份':
        flash('please enter the province.')
    elif request.form.get('city','') == '城市':
        flash('please enter the city.')
    elif form.validate_on_submit():
        user = models.User(request.form.get('email',''))
        user.username = request.form.get('username','')
        user.password = request.form.get('password','')
        user.gender = request.form.get('gender','')
        user.country = request.form.get('country','')
        user.province = request.form.get('province','')
        user.city = request.form.get('city','')
        user.moreaddress = request.form.get('moreaddress','')
        user.power = 2

        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        login_user(user,False)
        print token
        send_email(user.email, 'Confirm Your Account',
                   'email/confirm', user=user, token=url_for('confirm',token = token))
        flash(url_for('confirm',token = token))
        flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('login'))
    elif request.form.get('password','') != request.form.get('password2',''):
        flash('两次输入密码不一致.')
    elif request.form.get('gender','') is None:
        print 'please enter the gender.'
        flash('please enter the gender.')
    else:
        flash('请正确填写下述信息')



    return render_template('register.html', form=form)



@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='此网页的使用说明和其他信息——'
    )


@app.route('/user')
@login_required
def user():
    """Renders the user page."""
    return render_template(
        'user.html',
        title='User',
        year=datetime.now().year,
        message='用户主界面——'
    )

@app.route('/send')
@login_required
def send():
    """Renders the send page."""
    return render_template(
        'send.html',
        title='Send',
        year=datetime.now().year,
        message='我要寄信——'
    )

@app.route('/receive')
@login_required
def receive():
    """Renders the receive page."""
    return render_template(
        'receive.html',
        title='Receive',
        year=datetime.now().year,
        message='我要收信——'
    )



@app.route('/personal/<username>')
def personal(username):
    """Renders the personal page."""
    user=models.User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    else:
        username=user.username
        email=user.email
        gender=user.gender
        introduction=user.introduction

    return render_template(
        'personal.html',
        title='Personal',
        year=datetime.now().year,
        message='个人信息——',
        name=username,
        email=email,
        gender=gender,
        addr='玉泉29舍',
        information=introduction
    )


@app.route('/zonesend')
def zonesend(username):
    """Renders the zonesend page."""
    return render_template(
        'zonesend.html',
        year=datetime.now().year,
        message='',
        user_name='402吃鸡团队'#从数据库读
    )


@app.route('/zonereceive/<username>',methods=['GET','POST'])
def zonereceive(username):
    """Renders the zonereceive page."""
    user=models.User.query.filter_by(username=current_user.username).first()
    if user is None:
        abort(404)
    moment=Moment()
    form=forms.PostForm()
    if form.validate_on_submit():
        post=models.Post()
        post.body=form.body.data
        post.author_id=current_user.get_id()
        db.session.add(post)
        return redirect(url_for('zonereceive',username=current_user.username))
    posts=user.posts.order_by(models.Post.timestamp.desc()).all()
    #page=request.args.get('page',1,type=int)
    #pagination=models.Post.query.order_by(models.Post.timestamp.desc()).paginate(page, per_page=app.config['FLASKY_POSTS_PER_PAGE'],error_out=False)
    #posts=pagination.items
    return render_template(
        'zonereceive.html',
        user=user,
        form=form,
        posts=posts,
        moment=moment,
        current_user = current_user,
        #pagination=pagination
    )



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
"""
@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400	
"""


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


@app.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('You have confirmed your account. Thanks!')
    else:
        flash('The confirmation link is invalid or has expired.')
    return redirect(url_for('user'))



@app.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_email(current_user.email, 'Confirm Your Account',
               '/email/confirm', user=current_user, token=url_for(confirm,token = token))
    flash('A new confirmation email has been sent to you by email.')
    return redirect(url_for('user'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404layout.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500layout.html'), 500

if __name__ == '__main__':
    app.config.from_object('config')
    app.run()
    #manager.run()
