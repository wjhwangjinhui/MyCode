#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@author: wangjh
@software: PyCharm
@file: baidu_ocr.py
@time: 2019-03-16
"""
from aip import AipOcr

APP_ID = '你的APP_ID'
API_KEY = '你的API_KEY'
SECRET_KEY = '你的SECRET_KEY'


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def ocr_img(img_file):
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(img_file)
    ocr_data = client.basicAccurate(image)
    words_result = ocr_data['words_result']
    data = []
    for words in words_result:
        a = words['words']
        data.append(a)
    return data


if __name__ == '__main__':
    img_file = '3865a562ecb252ff81b35c3791de8ed.jpg'
    data = ocr_img(img_file)
    print(data)
