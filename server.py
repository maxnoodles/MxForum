# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
import tornado
from tornado import web
from tornado.ioloop import IOLoop
from peewee_async import Manager

from MxForum.urls import urlpattern
from MxForum.settings import settings, db

if __name__ == '__main__':
    # 集成 json 到 wtforms
    import wtforms_json
    wtforms_json.init()

    app = web.Application(urlpattern, debug=True, **settings)
    objects = Manager(db)
    app.objects = objects

    app.listen(8888)
    IOLoop.current().start()


