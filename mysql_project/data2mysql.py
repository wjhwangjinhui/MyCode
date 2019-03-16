#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@author: wangjh
@software: PyCharm
@file: data2mysql.py
@time: 2019-03-16
"""
from mysql_project.connect_mysql import DbHandle
from mysql_project.produce_sql import HandDb

db = DbHandle()


def persis_data_into_mysql(table, data):
    hd = HandDb(table)
    sql = hd.generate_sql_dict(data)
    db.insert_db_func(sql=sql)


if __name__ == '__main__':
    table = '表名'
    data = {'字段1': '值', '字段2': '值'}
    persis_data_into_mysql(table, data)
