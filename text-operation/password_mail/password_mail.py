import base64

from flask import Flask, abort, render_template, request
from flask_wtf import Form
from typing import Optional

app = Flask(__name__)


class MyForm(Form):
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        message = request.form.get('message', None)
        email = request.form.get('email', None)
        if message and email:
            encrypt_message = base64.b64encode(message.encode())
            # 846478339@qq.com
            send_email(email, encrypt_message.decode())
            return "something is ok"
        # do something
        return "something is error"
    abort(404)


def send_email(to, message):
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    _user = "1831353087@qq.com"
    _pwd = "******"  # 需要的密码是相关设置中开启IMAP/SMTP 的授权码
    # _pwd是授权码
    _to = to

    # 使用MIMEText构造符合smtp协议的header及body
    msg = MIMEText(message)
    msg["Subject"] = Header("password_mail", charset='utf-8')
    msg["From"] = _user
    msg["To"] = _to

    s = smtplib.SMTP_SSL(
        "smtp.qq.com", timeout=5, port=465)  # 连接smtp邮件服务器,端口默认是25
    s.login(_user, _pwd)  # 登陆服务器
    try:
        s.sendmail(_user, _to, msg.as_string())  # 发送邮件
    finally:
        s.close()
