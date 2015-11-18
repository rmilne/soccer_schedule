# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IcesportsItem(scrapy.Item):
    day = scrapy.Field()
    time = scrapy.Field()
    vistor = scrapy.Field()
    home = scrapy.Field()
    score = scrapy.Field()


