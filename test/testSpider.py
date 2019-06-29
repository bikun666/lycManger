import requests
from lxml import html


# 获取主页列表
def getPage():
    baseUrl = 'http://www.6vhao.net/'
    selector = html.fromstring(requests.get(baseUrl).content)

    urls = []
    for i in selector.xpath('//ul/'):
        urls.append(i)
    return urls

if __name__ == '__main__':
    urls = getPage()
    for url in urls:
        print(url)