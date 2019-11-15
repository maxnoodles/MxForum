# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
import json
from datetime import datetime
from random import choice

import jwt

from apps.users.forms import SmsCodeForm, RegisterForm, LoginForm
from apps.users.models import User
from apps.utils.YunPian import send_single_sms
from MxForum.handler import RedisHandler


class RegisterHandler(RedisHandler):

    async def post(self, *args, **kwargs):
        re_data = {}
        param = self.request.body.decode('utf8')
        register_form = RegisterForm.from_json(json.loads(param))
        if register_form.validate():
            mobile = register_form.mobile.data
            code = register_form.code.data
            password = register_form.password.data

            # 验证验证码
            redis_key = f'{mobile}_{code}'
            if not self.redis_conn.get(redis_key):
                self.set_status(400)
                re_data['code'] = '验证码错误或失效'
            else:
                # 验证用户是否存在
                try:
                    existed_user = await self.application.objects.get(User, mobile=mobile)
                    re_data['mobile'] = '用户已经存在'
                except User.DoesNotExist as e:
                    user = await self.application.objects.create(User, mobile=mobile, password=password)
                    re_data['id'] = user.id
        else:
            self.set_status(400)
            re_data = register_form.errors

        self.write(re_data)


class LoginHandler(RedisHandler):
    async def post(self, *args, **kwargs):
        re_data = {}

        param = self.request.body.decode('utf8')
        login_form = LoginForm.from_json(json.loads(param))
        if login_form.validate():
            mobile = login_form.mobile.data
            password = login_form.password.data
            try:
                user = await self.application.objects.get(User, mobile=mobile)
                if not user.password.check_password(password):
                    self.set_status(400)
                    re_data['non_fields'] = '用户名或者密码错误'
                else:
                    # 删除 jwt
                    payload = {
                        'id': user.id,
                        'nick_name': user.nick_name,
                        'exp': datetime.utcnow()
                    }
                    token = jwt.encode(payload, self.settings['SECRET'], algorithm='HS256')
                    re_data['id'] = user.id
                    if user.nick_name:
                        re_data['nick_name'] = user.nick_name
                    else:
                        re_data['nick_name'] = user.mobile
                    re_data['token'] = token.decode('utf8')
            except:
                self.set_status(400)
                re_data['mobile'] = '用户不存在'

        return self.write(re_data)


class SmsHandler(RedisHandler):
    @staticmethod
    def generate_code():
        """
        生成随机4位验证码
        :return:
        """
        seeds = '1234567890'
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return ''.join(random_str)

    async def post(self, *args, **kwargs):
        ret_data = {}

        param = self.request.body.decode('utf8')
        param = json.loads(param)
        sms_form = SmsCodeForm.from_json(param)
        if sms_form.validate():
            mobile = sms_form.data['mobile']
            code = self.generate_code()
            result = send_single_sms(code, mobile)
            if not result:
                self.set_status(400)
            else:
                # 讲验证码写入到 redis 中
                self.redis_conn.set(f'{mobile}_{code}', 1, ex=10*60)
            ret_data['send_sms'] = result
        else:
            self.set_status(400)
            ret_data = sms_form.errors

        return self.write(ret_data)


