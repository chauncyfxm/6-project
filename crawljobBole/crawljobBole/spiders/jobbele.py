# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobbeleSpider(CrawlSpider):
    name = 'jobbele'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    # "http://blog.jobbole.com/all-posts/page/3/"
    rules = (
        Rule(LinkExtractor(allow=r"http://blog.jobbole.com/all-posts/page/\d+/",restrict_xpaths=('//*[@id="archive"]/div[21]')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
