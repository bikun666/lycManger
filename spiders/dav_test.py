import webdav.client as wc

if __name__ == '__main__':
    options = {
        'webdav_hostname': "https://main-gongzuojp.ssl-lolipop.jp/owncloud/remote.php/webdav/",
        'webdav_login': "bikun",
        'webdav_password': "kunkun520"
        # 'keys':'login'
    }
    client = wc.Client(options=options)
    # client.upload_sync(remote_path="//webdav/", local_path="cookies.py")
    #
    # client.unpublish("dir1/file1.txt")
    # client.info("/test")
    # client.publish("/text/cookies.py")
    # client.upload_sync(remote_path="~/", local_path="cookies.py")
    print(client.list())
