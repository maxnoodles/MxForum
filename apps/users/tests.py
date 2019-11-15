# -*- coding:utf-8 -*-
#
# Copyright: yiguotech.com
# Author: chenjiaxin
# Date: 2019-11-14
import requests

web_url = 'http://127.0.0.1:8888'


def test_sms():
    url = f'{web_url}/code/'
    data = {
        'mobile': '13751678541'
    }
    res = requests.post(url, json=data)
    print(res.text)


def test_register():
    url = f'{web_url}/register/'
    data = {
        'mobile': '13751678541',
        'code': '9566',
        'password': '123'
    }
    res = requests.post(url, json=data)
    print(res.text)


def test_login():
    url = f'{web_url}/login/'
    data = {
        'mobile': '13751678541',
        'password': '123'
    }
    res = requests.post(url, json=data)
    print(res.text)


if __name__ == '__main__':
    # test_sms()
    # test_register()
    test_login()
