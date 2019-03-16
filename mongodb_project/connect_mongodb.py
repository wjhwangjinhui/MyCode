#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@author: wangjh
@software: PyCharm
@file: connect_mongodb.py
@time: 2019-03-16
"""
import pymongo

# 连接数据库
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client['test']


def save_data_in_mongo(data, table):
    table = db[table]
    table.insert_one(data)
