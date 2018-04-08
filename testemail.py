#-*- coding:utf-8 -*-
from flask import Flask,render_template
from flask.ext.mail import Mail,Message
import os
from threading import Thread


app = Flask(__name__)
#下面是SMTP服务器配置
app.config['MAIL_SERVER'] = 'smtp.163.com' #电子邮件服务器的主机名或IP地址
app.config['MAIL_PORT'] = 25 #电子邮件服务器的端口
app.config['MAIL_USE_TLS'] = True #启用传输层安全
app.config['MAIL_USERNAME'] = 'randu_group@163.com'
app.config['MAIL_PASSWORD'] = 'ZJU517'
mail = Mail(app)


def send_async_email(app,msg):
    with app.app_context():
        mail.send(msg)

		
@app.route('/')
def index():
    msg = Message('主题',sender='randu_group@163.com',recipients=['357634891@qq.com'])
    msg.body = '文本 body'
    msg.html = '<b>我是诈骗短信！</b> body'

    thread = Thread(target=send_async_email,args=[app,msg])
    thread.start()

    return '<h1>邮件发送成功</h1>'


if __name__ == '__main__':
    app.run(debug=True)
