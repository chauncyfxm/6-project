# -*- coding: utf-8 -*-
import scrapy
import json

# https://lvyou.baidu.com/main/ajax/rank/prod?type=1&t=1532000180028
# https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=35&rn=10&t=1532000316631
# https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=45&rn=10&t=1532000554199
# https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=55&rn=10&t=1532000570251
# https://lvyou.baidu.com/search/ajax/searchnotes?format=ajax&type=0&pn=65&rn=10&t=1532000575963





class LySpider(scrapy.Spider):
    name = 'ly'
    allowed_domains = ['lvyou.baidu.com']
    start_urls = ['https://lvyou.baidu.com/main/ajax/rank/prod?type=1&t=1532002870294']

    def parse(self, response):
        print(json.loads(response.text))
        pass
