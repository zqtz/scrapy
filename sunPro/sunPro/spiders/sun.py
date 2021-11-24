import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import sunItem,detailItem


class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']
    start_link = LinkExtractor(allow=r'page=\d+')
    detail_link = LinkExtractor(allow=r'id=\d+')

    rules = (
        Rule(start_link, callback='parse_item', follow=True),
        Rule(detail_link, callback='detail_item')
    )

    def parse_item(self, response):
        item = sunItem()
        li_lists = response.xpath('./')
        for li_list in li_lists:
            sun_id = li_list.xpath().extract()
            sun_title = li_list.xpath().extract()
            item['sun_id'] = sun_id
            item['sun_title'] = sun_title
            print(sun_id,sun_title)
            yield item

    def detail_item(self, response):
        item = detailItem()
        li_lists = response.xpath('./')
        for li_list in li_lists:
            detail_id = li_list.xpath().extract()
            detail_content = li_list.xpath().extract()
            item['sun_id'] = detail_id
            item['sun_title'] = detail_content
            print(detail_id, detail_content)
            yield item


