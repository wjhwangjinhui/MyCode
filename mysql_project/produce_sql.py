#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@author: wangjh
@software: PyCharm
@file: produce_sql.py
@time: 2019-03-16
"""


class HandDb(object):
    original_sql = """insert into {table_name}({columns}) values {column_values}"""

    def __init__(self, table):
        self.table = table

    def generate_sql_dict(self, item):
        """
        生产单条sql插入语句
        :param table: 表名
        :param item: 数据字典形式
        :return:
        """
        # print(item)
        if self.table == "tb_credit":
            item['credit_level'] = 'A'
        dbcol = []
        values = []
        for k in item:
            dbcol.append(k)
            values.append(item.get(k, ""))
        sql = self.original_sql.format(table_name=self.table, columns=",".join(dbcol), column_values=tuple(values))
        return sql

    def generate_sql_list(self, data, cols):
        """

        :param data: list
        :param cols: list
        :return:
        """
        if self.table == "tb_credit" and 'credit_level' not in cols:
            cols.append('credit_level')
            data.append("A")
        sql = self.original_sql.format(table_name=self.table, columns=",".join(cols), column_values=tuple(data))
        return sql
