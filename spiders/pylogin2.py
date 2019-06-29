import sys
import io
import urllib.request
import http.cookiejar
import requests


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码



def login_saba():

    url1 = "https://main-gongzuojp.ssl-lolipop.jp/owncloud/"
    # 初始化url请求对象
    r = requests.get(url1)
    # 获取url请求对象中的有用信息，如token、cookies
    token = r.cookies.items()[0][1]
    cookies = r.cookies
    # 以下为测试，所获取的token及cookie的格式
    print(type(token))
    print(token)
    print(cookies)
    print(r.headers)
    print(r.url)

    data = {
        'user':'bikun',
        'password':'kunkun520',
        'timezone-offset':'9',
        'timezone':'Asia/Tokyo',
        'cookie':'token=' + token}

    post_data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    login_url = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/'

    req = urllib.request.Request(login_url, headers = headers, data = post_data)

    cookie = http.cookiejar.CookieJar()

    #由cookie构造opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

    #发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    resp = opener.open(req)

    url = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php/apps/files/'

    req = urllib.request.Request(url, headers = headers)

    resp = opener.open(req)

    return resp.read().decode('utf-8')

if __name__ == '__main__':
    login_saba()