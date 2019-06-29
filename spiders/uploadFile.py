import urllib

from bs4 import BeautifulSoup

from spiders import login_owncloud



if __name__ == '__main__':


    session = login_owncloud.login('bikun','kunkun520')
    loginresponse = session.get('https://main-gongzuojp.ssl-lolipop.jp/owncloud/')

    homesoup = BeautifulSoup(loginresponse.text, "html.parser")
    requesttoken2 = homesoup.find('head').get('data-requesttoken')

    upload_headers = {
        'requesttoken': requesttoken2,
        'authority': 'main-gongzuojp.ssl-lolipop.jp',
        'method': 'PUT',
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
        'dir':'/remote.php/webdav/test',
        'file_directory':'',
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
        'dir':'/remote.php/webdav/test',

        'files':'["618IYwJvy4L._SL1200_.jpg"]'
    }


    upload_url = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php/apps/files/ajax/upload.php?dir=%2Ftest'
    delete_url = 'https://main-gongzuojp.ssl-lolipop.jp/owncloud/index.php/apps/files/ajax/delete.php'
    # print(loginresponse.text)
    # session.headers['Content-Type'] = m.content_type
    upload_data = urllib.parse.urlencode(upload_data).encode('utf-8')
    try:
        posts = session.put(url='https://main-gongzuojp.ssl-lolipop.jp/owncloud/remote.php/webdav/test', headers=upload_headers, data=upload_data)
        posts.encoding = 'unicode-escape'
        print(posts.text)
    except Exception as e:
        print(e)
    # pass