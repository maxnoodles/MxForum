# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
from peewee import *

from apps.users.models import User
from MxForum.settings import db


def init():
     db.create_tables([User])


if __name__ == '__main__':
    init()


