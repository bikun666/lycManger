# coding: utf8
import requests
from bs4 import BeautifulSoup
import time
import os
import urllib
from requests_toolbelt import MultipartEncoder
import base64

XLSX_MIMETYPE = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

class BufferReader(MultipartEncoder):
    """将multipart-formdata转化为stream形式的Proxy类
    """

    def __init__(self, fields, boundary=None, callback=None, cb_args=(), cb_kwargs=None):
        self._callback = callback
        self._progress = 0
        self._cb_args = cb_args
        self._cb_kwargs = cb_kwargs or {}
        super(BufferReader, self).__init__(fields, boundary)

    def read(self, size=None):
        chunk = super(BufferReader, self).read(size)
        self._progress += int(len(chunk))
        self._cb_kwargs.update({
            'size': self._len,
            'progress': self._progress
        })
        if self._callback:
            try:
                self._callback(*self._cb_args, **self._cb_kwargs)
            except:  # catches exception from the callback
                # raise CancelledError('The upload was cancelled.')
                pass
        return chunk



def main():
    headers = {
        'authority': 'main-gongzuojp.ssl-lolipop.jp',
        'method': 'POST',
        'path': '/owncloud/',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'cache-control': 'max-age=0',
        'content-length': '312',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'null',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }
    webUrl = "https://main-gongzuojp.ssl-lolipop.jp/owncloud/"
    data = {'is_org_page': 'false'}
    session = requests.session()
    resp = session.get(webUrl, data=data, headers=headers)
    homesoup = BeautifulSoup(resp.text, "html.parser")
    requesttoken1 = homesoup.find('head').get('data-requesttoken')
    loginurl = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php/apps/files/ajax/list.php?dir=%2FLYC05_%E9%99%B3%E5%BF%85%E5%9D%A4&sort=name&sortdirection=asc'
    data = {
        'user':'bikun',
        'password':'kunkun520',
        'timezone-offset':'100',
        'timezone':'Asia/Tokyo',
        'requesttoken':requesttoken1
    }

    post_data = urllib.parse.urlencode(data).encode('utf-8')
    loginresponse = session.post(url=webUrl, headers=headers, data=post_data)


    homesoup = BeautifulSoup(loginresponse.text, "html.parser")
    requesttoken2 = homesoup.find('head').get('data-requesttoken')

    upload_headers = {
        'requesttoken': requesttoken2,
        'authority': 'main-gongzuojp.ssl-lolipop.jp',
        'method': 'POST',
        'path': '/owncloud/index.php/apps/files/ajax/upload.php%2Ftest',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'content-length': '107384',
        'content-type': 'multipart/form-data; boundary=---------------------------191691572411478',
        'ocs-apirequest': 'true',
        'origin': 'https://main-gongzuojp.ssl-lolipop.jp',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }


    file_directory = 'demo01.jpg'
    fileDataBinary = open(file_directory, 'rb')
    files = {'uploadFile': (file_directory, fileDataBinary,"application/binary")}
    file_payload = {'uploadFile': ('demo01.jpg', open('demo01.jpg', 'rb'), "image/png")}
    file1 = {'file': open('demo01.jpg', 'rb')}
    # m = MultipartEncoder(file_payload)
    # m = MultipartEncoder(
    #     files={
    #         'field0': ('demo01.jpg', open('demo01.jpg', 'rb'), 'image/png')
    #     }
    # )

    # f = open('./demo01.jpg', 'rb')
    # f_str = base64.b64encode(f.read())
    # with open('D:\\Users\\kun\\PycharmProjects\\lycManger\\spiders\\demo01.jpg', 'rb') as f:
    #     str = base64.b64encode(f.read())

    # session.headers['content-type'] = 'multipart/form-data; boundary=----WebKitFormBoundary5n2pYAkCfb2wmlSr'
    # session.headers['x-requested-with'] = 'XMLHttpRequest'
    # upload_files = BufferReader(files)


    upload_data = {
        'requesttoken': requesttoken2,
        'dir':'/test',
        'file_directory':'./',
        'files[]':file1,
    }

    del_header = {
        'authority': 'main-gongzuojp.ssl-lolipop.jp',
        'method': 'POST',
        'path': '/owncloud/index.php/apps/files/ajax/delete.php',
        'scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'content-length': '54',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'ocs-apirequest': 'true',
        'origin': 'https://main-gongzuojp.ssl-lolipop.jp',
        'requesttoken': requesttoken2,
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }

    del_data = {
        'dir':'\/test',

        'files':'["618IYwJvy4L._SL1200_.jpg"]'
    }


    upload_url = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php/apps/files/ajax/upload.php?dir=%2Ftest'
    delete_url = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php/apps/files/ajax/delete.php'
    # print(loginresponse.text)
    # session.headers['Content-Type'] = m.content_type
    del_data = urllib.parse.urlencode(del_data).encode('utf-8')
    try:
        posts = session.post(url=upload_url, headers=upload_headers, data=upload_data)
        posts.encoding = 'unicode-escape'
        print(posts.text)
    except Exception as e:
        print(e)
    # pass


if __name__ == '__main__':
    main()
