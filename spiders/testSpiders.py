# Create your tests here.
from lxml import etree
from spiders import pylogin2


if __name__ == '__main__':
    # selector=etree.HTML()
    # content=selector.xpath('//*[@id="fileList"]/tr[4]/td[1]/a[2]/@href')
    # print(selector)
    print(pylogin2.login_saba())



