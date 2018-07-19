# -*- coding: utf-8 -*-
import scrapy
from ..items import JobboleprojectItem

class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = [
        'https://sou.zhaopin.com/jobs/searchresult.ashx?kw=df&sm=0&p=1',
        # 'https://sou.zhaopin.com',

    ]

    def parse(self, response):
        # print(response.status)
        # print(response.text)
        # print(response.content)
        # with open('zhilian.html','w') as f:
        #     f.write(response.text)
        # // *[ @ id = "newlist_list_content_table"] / table[2] / tbody / tr[1] / td[1] / div / a
        job_list = response.xpath('//*[@id="newlist_list_content_table"]//table')
        # print(job_list)
        # print(len(job_list))
        for item in job_list:
            url = item.xpath('.//td[@class="zwmc"]/div/a/@href').extract()
            if len(url)>0:
                url = url[0]
                print(url)
                yield scrapy.Request(url,callback=self.parse_job_detail)

        pass
    def parse_job_detail(self,response):
        # print(response.text)
        jobtitle = response.xpath('//div[@class="inner-left fl"]/h1/text()').extract()[0]
        salary = response.xpath('//div[@class="terminalpage clearfix"]//li[1]/strong/text()').extract()[0]
        publishTime = response.xpath('//div[@class="terminalpage clearfix"]//li[3]/strong/span/text()').extract()[0]
        workAdress = response.xpath('//div[@class="terminalpage clearfix"]//li[2]/strong/a/text()').extract()[0]
        # needpeople
        # response.xpath('//div[@]')



        print(jobtitle,salary,publishTime,workAdress)



