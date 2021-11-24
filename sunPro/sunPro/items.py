# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SunproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    def sunItem(self):
        sun_id = scrapy.Field()
        sun_title = scrapy.Field()

    def detailItem(self):
        detail_id = scrapy.Field()
        detail_content = scrapy.Field()
