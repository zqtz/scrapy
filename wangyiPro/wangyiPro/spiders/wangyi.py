import scrapy
from selenium import webdriver
from wangyiPro.items import WangyiproItem

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
        self.web = webdriver.Chrome(chrome_options=options)
        self.url_list = []

    def parse(self, response):
        li_lists = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        indexs = [3,4,6,7,8]
        for index in indexs:
            link = li_lists[index].xpath('./a/@href').extract_first()
            self.url_list.append(link)
            for url in self.url_list:
                yield scrapy.Request(url,callback=self.parse_mode)
        # li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        # allist = [3,4,6,7,8]
        # for index in allist:
        #     model_url = li_list[index].xpath('./a/@href').extract_first()
        #     self.url_list.append(model_url)
        #     for url in self.url_list:
        #         yield scrapy.Request(url,callback=self.parse_mode)

    def parse_mode(self,response):
        item = WangyiproItem()
        div_lists = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
        for div_list in div_lists:
            title = div_list.xpath('./div/div[1]/h3/a/text()').extract_first()
            link = div_list.xpath('./div/div[1]/h3/a/@href').extract_first()
            item['title'] = title
            yield scrapy.Request(url=link,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self,response):
        item = response.meta['item']
        content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
        content = ''.join(content)
        item['content'] = content
        yield item

    def close(self,spider):
        self.web.quit()

# -*- coding: utf-8 -*-
# import scrapy
# from selenium import webdriver
# from wangyiPro.items import WangyiproItem
#
# class WangyiSpider(scrapy.Spider):
#     name = 'wangyi'
#     # allowed_domains = ['www.xxx.com']
#     start_urls = ['https://news.163.com/']
#
#     def __init__(self):
#         option = webdriver.ChromeOptions()
#         # 防止打印一些无用的日志
#         option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
#         self.web = webdriver.Chrome(chrome_options=option)
#         self.model_urls = []
#
#     def parse(self, response):
#         # //*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul
#         li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
#         allist = [3,4,6,7,8]
#         for index in allist:
#             model_url = li_list[index].xpath('./a/@href').extract_first()
#             self.model_urls.append(model_url)
#             for url in self.model_urls:
#                 yield scrapy.Request(url,callback=self.parse_model)
#
#     def parse_model(self,response):
#         # /html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div
#         div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div[1]/div/ul/li/div/div')
#         for div in div_list:
#             title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
#             model_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()
#             item = WangyiproItem()
#             item['title'] = title
#             yield scrapy.Request(url=model_detail_url,callback=self.parse_detail,meta={'item':item})
#     def parse_detail(self,response):
#         # //*[@id="content"]/div[2]
#         content = response.xpath('//*[@id="content"]/div[2]//text()').extract()
#         content = ''.join(content)
#         item = response.meta['item']
#         item['content'] = content
#         yield item
#
#     def closed(self,spider):
#         self.web.quit()


