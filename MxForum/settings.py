# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
import peewee_async

settings = {
    'static_path': r'C:\a_cjx\python_work\MxForum\static',
    'static_url_prefix': '/static/',
    'SECRET': 'Vx0QyzNhvQhFBrJd',
    'db': {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'root',
        'database': 'mxforum',
        'port': 3306
     },
    'redis': {
        'host': '127.0.0.1',
        'charset': 'utf8'
    }
}

db = peewee_async.PooledMySQLDatabase(**settings['db'])


