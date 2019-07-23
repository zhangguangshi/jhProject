import MySQLdb
import requests
from lxml import etree
from urllib.request import urljoin

class VideoSpider(object):
    connect = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="123456",db="jhweb",use_unicode=True,charset="utf8")
    cursor = connect.cursor()
    base_url = "http://www.farmer.com.cn/xwpd/btxw/"
























