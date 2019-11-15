# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
from tornado.web import url


urlpattern = (
    url('/groups/', SmsHandler),
    url('/register/', RegisterHandler),
    url('/login/', LoginHandler)
)
