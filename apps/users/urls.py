# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
from tornado.web import url
from apps.users.handler import SmsHandler, RegisterHandler, LoginHandler

urlpattern = (
    url('/code/', SmsHandler),
    url('/register/', RegisterHandler),
    url('/login/', LoginHandler)
)
