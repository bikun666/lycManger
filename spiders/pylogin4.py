import sys
import io
import urllib.request
import http.cookiejar


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def login_saba():
    data = {
        'user':'xxx',
        'password':'xxxxxx',
        'timezone-offset':'9',
        'timezone':'Asia/Tokyo',
        'requesttoken':'7ec80c677734b13878babe27f76a751f6e8682f4d0c6e6da6170b0e9757c4fb6|jP8CNFA5czlKcJLZ|32c83bb34c7852f1a6428613747c3cc501b80e1278e613cf718bbd8eb5ea2d24d363ef48b4f762a318155c7af357f05fddaa40a1337c9f483b27617339d4fdbd:rJ65afkAfn'}

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
    print(login_saba())