#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
# 导入自定义表单需要的字段
from wtforms import SubmitField, StringField, PasswordField

# 导入wtf扩展提供的表单验证器
from wtforms.validators import DataRequired, EqualTo

# 解决编码问题，将所有字段都设置为utf-8
# 故不用再在有编码问题的字段前加u
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.secret_key = 'love'
"""
目的：实现简单的登录的逻辑处理
1、 路由需要有get和post两种请求
2、 获取请求的参数
3、 判断参数是否填写，密码是否相同
4、 判断都没问题则返回success
"""
'''
使用flash给模板传递消息，需要对消息内容加密
所以需要设置secret_key
所以需要设置secret_key
'''

'''
使用wtf实现表单
自定义表单类
'''


class LoginForm(FlaskForm):
    # validators验证有值
    username = StringField('用户名:', validators = [DataRequired()])
    password = PasswordField('密码:', validators = [DataRequired()])
    # EqualTo第一个参数表示和谁比较，第二参数表示不一致时的显示
    password2 = PasswordField('确认密码:', validators = [DataRequired(), EqualTo('password', '密码输入不一致')])
    submit = SubmitField('提交')

@app.route('/form', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # # 测试
        # return "%d" % (login_form.validate_on_submit())

        if login_form.validate_on_submit():
            flash(username)
            flash(password)
            return "success"
        else:
            flash('参数有误')
    return render_template('index.html', form = login_form)

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    # 判断请求方式
    if request.method == 'POST':
        # 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print username, password

        # 判断请求参数是否填写，且密码是否相同
        if not all([username, password, password2]):
            # print "参数不完整"
            flash(u"参数不完整")
        elif password != password2:
            # print "密码不一致"
            flash(u"密码不一致")
        else:
            return "success"
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
