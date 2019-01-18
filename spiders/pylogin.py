import sys
import io
import urllib.request
import http.cookiejar


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def login_saba():
    data = {'redirect_url':'/owncloud/index.php/apps/files/',
        'user':'bikun',
        'password':'kunkun520',
        'timezone-offset':'9',
        'timezone':'Asia/Tokyo',
        'requesttoken':'d45e83179c5c95e2c066d7265392ff6c7b19a264198070a5cea8b8fdade52ff0|jBL1p+mCsO5yM/5p|677af760f0ff188b6bf892576b065df805b3ea47735d67dafdbd9f53b3fe967b67a843249d9a3130f5b2893349852ac5a531d060180152f85165a15d29e5eb67:qNPnCGjsoj'}

    post_data = urllib.parse.urlencode(data).encode('utf-8')

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    login_url = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php?redirect_url=%2Fowncloud%2Findex.php%2Fapps%2Ffiles%2F'

    req = urllib.request.Request(login_url, headers = headers, data = post_data)

    cookie = http.cookiejar.CookieJar()

    #由cookie构造opener
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))

    #发送登录请求，此后这个opener就携带了cookie，以证明自己登录过
    resp = opener.open(req)

    url = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php/apps/files/'

    req = urllib.request.Request(url, headers = headers)

    resp = opener.open(req)

    return(resp.read().decode('utf-8'))