# -*- coding: utf-8 -*-

# Scrapy settings for CrawlBDlvyou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'CrawlBDlvyou'

SPIDER_MODULES = ['CrawlBDlvyou.spiders']
NEWSPIDER_MODULE = 'CrawlBDlvyou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'CrawlBDlvyou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/67.0.3396.99 Chrome/67.0.3396.99 Safari/537.36',
    'Cookie': 'BAIDUID=D70C5FA9CFB05FABFC56018BA2AE2F13:FG=1; BIDUPSID=D70C5FA9CFB05FABFC56018BA2AE2F13; PSTM=1531976546; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; FP_UID=968401e8b4ae6266be7a1343d53b91d3; BDUSS=nM1R0ZtaThaWFJOYUJ5UElWWFQ4ZUNKTDJUYjZvbWtiSVlUTWVJeElsQ2h3SGRiQUFBQUFBJCQAAAAAAAAAAAEAAADjqemGudjT2rratrQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKEzUFuhM1BbY; cflag=13%3A3; BDLVMONTH=VISITTIME=1531997336314; bdshare_firstime=1531997336358; H_PS_PSSID=1462_25810_21098_26350_22159; BCLID=15987190386381261436; BDSFRCVID=F10sJeC62lX59qO7_JxHuRp5S2WQXnnTH6aoaN43kasAiagSjPtnEG0Pqf8g0Ku-J0QOogKKXgOTHw3P; H_BDCLCKID_SF=tRk8oI-XJCvjD4-k247Hhn8thmT22-usWnvCQhcH0hOWsIOqeDF5jp4p2M7DQ-u8-5cmLbcH3tt5eDbxDUC0DTbbDGKJtjn2ajPXXJnqa-JED6rnhPF3Q6oQKP6-35KHaN-tV4jvJM7kJhnG0R0h0TDi0J7X2q37JD6y3lu2tbvHqpjY-tJ6Ml83h4oxJpOD5JbMopvaHlF2Vq7vbURvW--g3-7fJh8EK5r2SC_btIKb3H; PSINO=1; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; Hm_lvt_46c590aaade82326fc76f3ed3ed69f98=1531997337,1532077246,1532077255,1532077550; BDLVYEAR=VISITTIME=1531997336314&LV_SCENE_PLAN_TIP=1; bdstoken=95ad8341b1de62a3674e16987586dc13; t=1532077730; BDLVDAY=VISITTIME=1532079063023; Hm_lpvt_46c590aaade82326fc76f3ed3ed69f98=1532079063',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'CrawlBDlvyou.middlewares.CrawlbdlvyouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'CrawlBDlvyou.middlewares.CrawlbdlvyouDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'CrawlBDlvyou.pipelines.CrawlbdlvyouPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
