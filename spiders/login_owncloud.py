# coding: utf8
import requests
from bs4 import BeautifulSoup
import time
import os
import urllib
from requests_toolbelt import MultipartEncoder
import base64

def login(user,pw):
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
    # loginurl = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php/apps/files/ajax/list.php?dir=%2FLYC05_%E9%99%B3%E5%BF%85%E5%9D%A4&sort=name&sortdirection=asc'
    data = {
        'user':user,
        'password':pw,
        'timezone-offset':'100',
        'timezone':'Asia/Tokyo',
        'requesttoken':requesttoken1
    }

    post_data = urllib.parse.urlencode(data).encode('utf-8')
    loginresponse = session.post(url=webUrl, headers=headers, data=post_data)
    return session
    # pass


if __name__ == '__main__':
    session = login('bikun','kunkun520')
    print(session.get('https://main-gongzuojp.ssl-lolipop.jp/owncloud/').text)
