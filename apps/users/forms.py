# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
from wtforms_tornado import Form
from wtforms import StringField
from wtforms.validators import DataRequired, Regexp, Length

MOBILE_REGEX = r'^1\d{10}$'


class SmsCodeForm(Form):
    mobile = StringField('手机号码', validators=[DataRequired(), Regexp(MOBILE_REGEX)])


class RegisterForm(SmsCodeForm):
    code = StringField('验证码', validators=[DataRequired(), Length(max=4, min=4)])
    password = StringField('密码', validators=[DataRequired()])


class LoginForm(SmsCodeForm):
    password = StringField('密码', validators=[DataRequired()])

