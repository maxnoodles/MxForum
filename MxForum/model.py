# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
from datetime import datetime

import peewee_async
from peewee import *

from MxForum.settings import settings, db

objects = peewee_async.Manager(db)


class BaseModel(Model):
    create_time = DateTimeField(default=datetime.now, verbose_name='创建时间')

    def set_attr(self):
        pass

    class Meta:
        database = db

