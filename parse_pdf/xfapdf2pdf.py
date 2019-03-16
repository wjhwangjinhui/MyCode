#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
@author: wangjh
@software: PyCharm
@file: xfapdf2pdf.py
@time: 2019-03-16
"""
import time
import requests
# 导入requests_toolbelt库使用MultipartEncoder
from requests_toolbelt import MultipartEncoder


def upload_pdf(localfile):
    url = 'https://speedtesting.herokuapp.com/pdfxfa/upload.php'
    headers = {
        'Origin': "https://speedtesting.herokuapp.com",
        'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 Safari/537.36",
        'Content-Type': "multipart/form-data; boundary=----WebKitFormBoundaryxAAua9MgkUszgIdT",
        'Accept': "*/*",
        'Referer': "https://speedtesting.herokuapp.com/pdfxfa/",
        'Connection': "keep-alive",
        'DNT': "1",
        'cache-control': "no-cache",
    }
    # file_payload = {'file': open('./financial.pdf', 'rb')}
    file_payload = {'file1': (localfile, open(localfile, 'rb')), 'name': 'financial.pdf'}
    # 生成可用于multipart/form-data上传的数据
    m = MultipartEncoder(file_payload)
    # 自动生成Content-Type类型和随机码
    headers['Content-Type'] = m.content_type
    # 使用data上传文件
    html = requests.post(url, headers=headers, data=m)
    return html.json()


def xfa_to_normal(resultFile):
    url = 'https://speedtesting.herokuapp.com/pdfxfa/upload.php?action=getresults'
    headers = {
        'Origin': "https://speedtesting.herokuapp.com",
        'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/72.0.3626.121 Safari/537.36",
        'Content-Type': "multipart/form-data; boundary=----WebKitFormBoundaryxAAua9MgkUszgIdT",
        'Accept': "*/*",
        'Referer': "https://speedtesting.herokuapp.com/pdfxfa/",
        'Connection': "keep-alive",
        'DNT': "1",
        'cache-control': "no-cache",
    }
    # file_payload = {'file': open('./financial.pdf', 'rb')}
    file_payload = {'resultfile': resultFile}
    # 生成可用于multipart/form-data上传的数据
    m = MultipartEncoder(file_payload)
    # 自动生成Content-Type类型和随机码
    headers['Content-Type'] = m.content_type
    # 使用data上传文件
    html = requests.post(url, headers=headers, data=m)
    return html.json()


def downloadFile(name, url):
    headers = {'Proxy-Connection': 'keep-alive'}
    r = requests.get(url, stream=True, headers=headers)
    length = float(r.headers['content-length'])
    f = open(name, 'wb')
    count = 0
    count_tmp = 0
    time1 = time.time()
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
            count += len(chunk)
            if time.time() - time1 > 2:
                p = count / length * 100
                speed = (count - count_tmp) / 1024 / 1024 / 2
                count_tmp = count
                print(name + ': ' + formatFloat(p) + '%' + ' Speed: ' + formatFloat(speed) + 'M/S')
                time1 = time.time()
    f.close()


def formatFloat(num):
    return '{:.2f}'.format(num)


if __name__ == '__main__':
    data = upload_pdf('test.pdf')
    resultfile = data.get('resultfile')
    result = xfa_to_normal(resultfile)
    download_url = result.get('destfile_enc')
    name = result.get('destfile_name')
    downloadFile(name, download_url)
