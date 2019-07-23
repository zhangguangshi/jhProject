# -*- coding:utf-8 -*-
"""
梅花香自苦寒来！
Author:zhang G.S
Time:  2019/2/23 10:35
File Name: news_spider
"""

import MySQLdb
import requests
from lxml import etree
from urllib.request import urljoin

class NewSpider(object):
    connect = MySQLdb.connect(host="localhost",port=3306,user="root",passwd="123456",db="jhweb",use_unicode=True,charset="utf8")
    cursor = connect.cursor()
    base_url = "http://www.farmer.com.cn/xwpd/btxw/"
    def __init__(self,page_num,site):
        self.page = page_num
        self.site = site

    def get_neweb(self):
        for index in range(0,self.page):
            url = self.base_url+'index_%s.htm'%index
            response = requests.get(url).text
            html = etree.HTML(response)
            div_list = html.xpath('//div[@class="yui3-g list-list-li"]')
            for div in div_list:
                title = div.xpath('.//a/text()')[0]
                time = div.xpath('.//span/text()')[0]
                href = div.xpath('.//a/@href')[0]
                url =  urljoin(self.base_url,href)
                print(title,time)
                self.cursor.execute("insert into news(title,href,origin,descrip,time,picture,type_id) values('%s','%s','头条新闻','%s','%s','%s',%d)"%(title,url,title,time,"/news/2019/03/13/14931977476361_index1.jpg",self.site))

        self.connect.commit()
        self.cursor.close()
        self.cursor.close()

if __name__ == '__main__':
    num = input("请输入爬取页数:")
    site= input("请输入插入号码:")
    new = NewSpider(int(num),int(site))
    new.get_neweb()





