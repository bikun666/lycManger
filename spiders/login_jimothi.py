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
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'ja-JP,ja;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Content-Length':'244',
        'Content-Type':'application/x-www-form-urlencoded',
        'Cookie':'device_uuid=d5dd86a8-b9b8-4ebe-8b54-36e860a4f081; uid=CgAETllKTtpj0xCAAydzAg==; _tdim=d1ea390a-ec11-4c17-e229-25e898276157; __gads=ID=305edcac9cbc8578:T=1520088393:S=ALNI_MauV4X2jUW-I4qjbGFU0UMgbVfrXA; cto_lwid=4ee0c4fe-4e4f-48e0-a72d-f3aaf045be34; _ga=GA1.2.767733135.1498042079; _fbp=fb.1.1547968682258.668472419; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.266750301.1547968685; _session_id=BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiJWNlYmNmMDVlMjA2ODliMmEzN2ZlMDU1MzM2YjNjZjgwBjsAVEkiE3JlY2VudF9oaXN0b3J5BjsARlsPewY6CGtleUkiCmJtN3A0BjsAVHsGOwZJIgpiNHN0awY7AFR7BjsGSSIKYjkwNmEGOwBUewY7BkkiCmI5MDhjBjsAVHsGOwZJIgpiOWhiZQY7AFR7BjsGSSIKYjloZHUGOwBUewY7BkkiCmFsc2c0BjsAVHsGOwZJIgpicmN6NwY7AFR7BjsGSSIKYnJkMGcGOwBUewY7BkkiCmJycHo4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMXczOXptbWlIeC81dUh0VndWZ2ZLNGgrOEZYVDVkL3dhYmlOeVNCVks1dWM9BjsARg%3D%3D--34f09f3cc90d1502c2d0f5c2d0a43a08778a0f79; _td=993c66b4-97ed-4a80-a166-77f213c88900',
        'Host':'jmty.jp',
        'Origin':'https://jmty.jp',
        'Referer':'https://jmty.jp/users/sign_in',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    webUrl = "https://jmty.jp/users/sign_in"
    data = {'is_org_page': 'false'}
    session = requests.session()
    resp = session.get(webUrl, data=data, headers=headers)
    homesoup = BeautifulSoup(resp.text, "html.parser")
    authenticity_token = homesoup.find('input', {'name': 'authenticity_token'})
    authenticity_token_v = authenticity_token['value']
    loginurl = 'https://jmty.jp/my/posts'
    data = {
        'utf8': '✓',
        'authenticity_token': authenticity_token_v,
        'user[email]': '260301507@qq.com',
        'user[password]': 'kunkun520',
        'user[remember_me]': '0',
        'user[remember_me]': '1'
    }
    post_data = urllib.parse.urlencode(data).encode('utf-8')
    loginresponse = session.post(url=webUrl, headers=headers, data=post_data)
    posts = session.post(url=loginurl, headers=headers, data=post_data)
    print(posts.text)
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