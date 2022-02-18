# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    sun_id = scrapy.Field()
    sun_title = scrapy.Field()
    # define the fields for your item here like:


class DetailItem(scrapy.Item):
    detail_id = scrapy.Field()
    detail_content = scrapy.Field()



