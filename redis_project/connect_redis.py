#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@author: wangjh
@software: PyCharm
@file: connect_redis.py
@time: 2019-03-16
"""
import platform
import redis

pl = platform.system()


class Connect_redis(object):
    def __init__(self, db):
        self.db = db

    def connect(self):
        if pl == "Linux":
            redis_obj = redis.Redis(host='127.0.0.1', port=6379, db=self.db)
        else:
            redis_obj = redis.Redis(host='127.0.0.1', port=6379, db=self.db)
        return redis_obj


class RedisPool:
    if pl == "Windows":
        def __init__(self, client_host="127.0.0.1", client_port=6379, client_db=0):
            self.client_host = client_host
            self.client_port = client_port
            self.client_db = client_db
    else:
        def __init__(self, client_host="127.0.0.1", client_port=6379, client_db=0):
            self.client_host = client_host
            self.client_port = client_port
            self.client_db = client_db

    def redis_pool(self):
        if pl == "Windows":
            pool = redis.ConnectionPool(
                host=self.client_host,
                port=self.client_port,
                db=self.client_db)
        else:
            pool = redis.ConnectionPool(
                host=self.client_host,
                port=self.client_port,
                db=self.client_db)
        return redis.StrictRedis(connection_pool=pool)
