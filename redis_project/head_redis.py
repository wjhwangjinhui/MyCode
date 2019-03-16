#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@author: wangjh
@software: PyCharm
@file: head_redis.py
@time: 2019-03-16
"""
from redis_project.connect_redis import RedisPool


class HandleRedis(object):
    def __init__(self, db):
        self.db = db
        self.redisobj = RedisPool(client_db=self.db)
        self.redispool = self.redisobj.redis_pool()

    def cache_dict_redis(self, k, data):
        """
        将数据存到redis以集合的形式存储
        :param k:
        :param data:
        :return:
        """
        redisobj = RedisPool(client_db=self.db)
        redispool = self.redisobj.redis_pool()
        if not isinstance(data, dict):
            raise ValueError
        redispool.sadd(k, data)
        print("cache redis success k is:%s" % k)

    def cache_list_redis(self, k, datas):
        """

        将列表数据以集合的形式缓存到redis
        :param k:
        :param datas:
        :return:
        """

        if not isinstance(datas, list):
            raise ValueError("缓存的数据不是list存在错误..........")
        self.redispool.sadd(k, *datas)
        print("cache redis success k is:%s,length is:%d" % (k, len(datas)))

    def get_data_redis(self, k):
        value = self.redispool.spop(k)
        if value:
            value = value.decode()
            return value
        else:
            return None

    def get_many_data_redis(self, k):
        values = self.redispool.srem(k, '5', '6')
        if values:
            return values

    def put_str_into_redis(self, k, data):
        self.redispool.sadd(k, data)
        print("cache redis success key is:%s" % k)

    def spop_data_from_redis(self, k):
        data = self.redispool.spop(k)
        if data:
            return data

    def get_length(self, k):
        # 获取键k里有多少条数据
        num = self.redispool.scard(k)
        if num:
            return num
        else:
            return None
