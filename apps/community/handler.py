# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
from tornado.web import RequestHandler, authenticated


from MxForum.handler import RedisHandler


class GroupHandler(RedisHandler):
    @authenticated
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass



