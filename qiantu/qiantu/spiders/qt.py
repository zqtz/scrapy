# -*- coding: utf-8 -*-
import scrapy
from qiantu.items import QiantuItem


class QtSpider(scrapy.Spider):
    name = 'qt'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://desk.zol.com.cn/dongman/1920x1080/1.html']

    def parse(self, response):
        item = QiantuItem()
        div_lists = response.xpath('//ul[@class="pic-list2  clearfix"]/li')
        for div_list in div_lists:
            link = div_list.xpath('./a/img/@src').extract()[0]
            print(link)
            item['link'] = link
            yield item

        for page in range(2,22):
            url = 'https://desk.zol.com.cn/dongman/1920x1080/'+str(page)+'.html'
            yield scrapy.Request(url,callback=self.parse)


