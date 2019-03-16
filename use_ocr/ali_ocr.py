#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

"""
@author: wangjh
@software: PyCharm
@file: ali_ocr.py
@time: 2019-03-16
"""

import requests
import json
import base64


def get_img_base64(img_file):
    with open(img_file, 'rb') as infile:
        base64_data = base64.b64encode(infile.read())
        img = str(base64_data)[2:-1]
        return img


def predict(url, appcode, img_base64, kv_config, old_format):
    if not old_format:
        param = {}
        param['image'] = img_base64
        if kv_config is not None:
            param['configure'] = json.dumps(kv_config)
        body = json.dumps(param)
    else:
        param = {}
        pic = {}
        pic['dataType'] = 50
        pic['dataValue'] = img_base64
        param['image'] = pic

        if kv_config is not None:
            conf = {}
            conf['dataType'] = 50
            conf['dataValue'] = json.dumps(kv_config)
            param['configure'] = conf

        inputs = {"inputs": [param]}
        body = json.dumps(inputs)

    headers = {'Authorization': 'APPCODE %s' % appcode}
    response = requests.post(url=url, headers=headers, data=body)
    return response.status_code, response.headers, response.text


def demo(img_file):
    appcode = '你的appcode'
    url = 'https://form.market.alicloudapi.com/api/predict/ocr_table_parse'
    # 如果输入带有inputs, 设置为True，否则设为False
    is_old_format = False
    config = {'format': 'json', 'finance': False, 'dir_assure': True}
    # 如果没有configure字段，config设为None
    # config = None

    img_base64data = get_img_base64(img_file)
    stat, header, content = predict(url, appcode, img_base64data, config, is_old_format)
    if stat != 200:
        print('Http status code: ', stat)
        print('Error msg in header: ', header['x-ca-error-message'] if 'x-ca-error-message' in header else '')
        print('Error msg in body: ', content)
        exit()
    if is_old_format:
        result_str = json.loads(content)['outputs'][0]['outputValue']['dataValue']
    else:
        result_str = content

    return result_str
    # result = json.loads(result_str)


if __name__ == '__main__':
    img_file = '3865a562ecb252ff81b35c3791de8ed.jpg'
    result_str = demo(img_file)
    result = json.loads(result_str)
    print(result)
