#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@author: wangjh
@software: PyCharm
@file: example.py
@time: 2019-03-16
"""
from redis_project.head_redis import HandleRedis


def use_example(db, key):
    r = HandleRedis(db)
    key = r.get_data_redis(key)


if __name__ == '__main__':
    db = 1  # 数据库
    key = "键"
    use_example(db, key)
