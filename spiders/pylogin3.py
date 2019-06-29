# coding: utf8
import requests
from bs4 import BeautifulSoup
import time
import os
import urllib

class Jm(object):
    def __init__(self, headers):
        self.headers = headers;
        self.session = requests.session()
        pass





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
    requesttoken = homesoup.find('head').get('data-requesttoken')
    loginurl = 'https://jmty.jp/my/posts'
    data = {
        'user':'bikun',
        'password':'kunkun520',
        'timezone-offset':'100',
        'timezone':'Asia/Tokyo',
        'requesttoken':requesttoken
    }

    post_data = urllib.parse.urlencode(data).encode('utf-8')
    loginresponse = session.post(url=webUrl, headers=headers, data=post_data)
    # posts = session.post(url=loginurl, headers=headers, data=post_data)
    print(loginresponse.text)
    # if loginresponse.json()['r'] == 1:
    #     self.getCap()
    #     captcha = input('请输入验证码：')
    #     postdata['captcha'] = captcha
    #     loginresponse = self.session.post(url=loginurl, headers=self.headers, data=postdata)
    #     print('服务器端返回响应码：', loginresponse.status_code)
    #     print(loginresponse.json())
    # profileurl = 'https://www.zhihu.com/settings/profile'
    # profileresponse = self.session.get(url=profileurl, headers=self.headers)
    # print('profile页面响应码：', profileresponse.status_code)
    # profilesoup = BeautifulSoup(profileresponse.text, 'html.parser')
    # div = profilesoup.find('div', {'id': 'rename-section'})


    pass


if __name__ == '__main__':
    main()