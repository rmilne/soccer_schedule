# -*- coding: utf-8 -*-
import scrapy


class FutureSpider(scrapy.Spider):
    name = "future"
    allowed_domains = ["soccer.icesports.com"]
    start_urls = ()

    # scrapy crawl future -a url='http://soccer.icesports.com/schedule-p...'
    def __init__(self, url=None, *args, **kwargs):
        super(FutureSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['%s' % url]

    def parse(self, response):
        pass
