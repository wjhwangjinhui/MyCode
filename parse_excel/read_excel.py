#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
@author: wangjh
@software: PyCharm
@file: read_excel.py
@time: 2019-03-16
"""
import xlrd


def xl2json(file):
    workbook = xlrd.open_workbook(file)
    names = workbook.sheet_names()
    data_list = []
    for i in range(len(names) - 1):
        data = {}
        name = names[i]
        data["sheet_name"] = name
        data["d"] = []
        worksheet = workbook.sheet_by_name(names[i])
        nrows = worksheet.nrows
        for j in range(2, nrows):
            d1 = worksheet.row_values(1)
            d = worksheet.row_values(j)
            a = {}
            for k in range(2, len(d)):
                a[d1[k]] = d[k]
            data["d"].append(a)
        data_list.append(data)
    return data_list
