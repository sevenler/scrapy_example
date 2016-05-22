#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一个简单的Python 爬虫, 用于抓取豆瓣电影Top前250的电影的名称描述等

Anthor: Andrew Liu
Version: 0.0.3
Date: 2014-12-17
Language: Python2.7.8
Editor: Sublime Text2
Operate: 具体操作请看README.md介绍
"""

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from douban.items import DoubanItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
import scrapy

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class DoubanSpider(CrawlSpider) :

    name = "douban"
    start_urls = ["https://www.douban.com/group/explore"]
    allowed_domains = ["www.douban.com"]

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            request = scrapy.Request(url, callback=self.parse)
            request.cookies['over18'] = 1
            request.headers['User-Agent'] = (
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, '
                'like Gecko) Chrome/45.0.2454.85 Safari/537.36'
            )
            yield request

    def parse(self, response) :
        sel = Selector(response)
        item = DoubanItem()
        print "********************"
        print sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()
        #item['name'] = sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()
        #item['description'] = sel.xpath('//div/span[@property="v:summary"]/text()').extract()
        #item['url'] = response.url
        return item
