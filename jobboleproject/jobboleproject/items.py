# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobboleprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobtitle = scrapy.Field()
    salary = scrapy.Field()
    publishTime = scrapy.Field()
    workAdress = scrapy.Field()
    jobDesc = scrapy.Field()
    companyName = scrapy.Field()
    companyUrl = scrapy.Field()
    pass

class ZhilianCompanItem(scrapy.Item):
    comapyName = scrapy.Field()
    comapyClasssfiy = scrapy.Field()
    comapyMode = scrapy.Field()
    comapyIndustry = scrapy.Field()
    comapyAdress = scrapy.Field()
    comapyDesc = scrapy.Field()

