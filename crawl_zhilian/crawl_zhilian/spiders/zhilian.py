# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ZhilianSpider(CrawlSpider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=530&bj=4010200&sj=008']

    # "http://jobs.zhaopin.com/CC121097227J00060838711.htm?ssidkey=y&amp;ss=201&amp;ff=03&amp;sg=5be8a0c7a6ee44708f74f0868de82539&amp;so=2"

    # "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=530&amp;bj=4010200&amp;sj=008&amp;sg=5be8a0c7a6ee44708f74f0868de82539&amp;p=2"
    rules = (
        Rule(LinkExtractor(allow=r'http://sou.zhaopin.com/jobs/searchresult.ashx?.*?p=\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r"http://jobs.zhaopin.com/CC121097227J00060838711.htm?ssidkey=y&amp;ss=201&amp;ff=03&amp;sg=5be8a0c7a6ee44708f74f0868de82539&amp;so=2"), callback='parse_item1',follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
    def parse_item1(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
