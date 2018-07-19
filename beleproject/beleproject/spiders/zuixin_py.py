# -*- coding: utf-8 -*-
import scrapy
from ..items import BeleprojectItem

class ZuixinPySpider(scrapy.Spider):
    name = 'zuixin_py'
    allowed_domains = ['blog.jobbole.com/']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        list = response.xpath('//div[@id="archive"]/div[@class="post floated-thumb"]')
        item = BeleprojectItem()
        for div in list:
            # 标题
            title1 = div.xpath('./div[2]/p[1]/a[1]/text()').extract()
            if len(title1) > 0:
                item['title'] = title1[0]
            # 日期
            datetime1 = div.xpath('./div[2]/p[1]/text()').extract()
            if len(datetime1) > 0:
                item['datetime'] = ''.join(datetime1).strip()
            # 分类
            type1 = div.xpath('./div[2]/p[1]/a[2]/text()').extract()
            if len(type1) > 0:
                item['type'] = type1[0]
            # 简介
            content1 = div.xpath('./div[2]/span/p/text()').extract()
            if len(content1) > 0:
                item['content'] = content1[0]
            yield item
        # 下一页
        # url1 = response.xpath('//*[@id="archive"]/div[21]/a[4]/@href').extract()
        url1 = response.xpath('//a[@class="next page-numbers"]/@href').extract()
        if len(url1)>0:
            url = url1[0]
        print(url+'*'*50)
        yield scrapy.Request(url,callback=self.parse,dont_filter=True)
        pass