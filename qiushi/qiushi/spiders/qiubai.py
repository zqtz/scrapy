import scrapy
from qiushi.items import QiushiItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/']

    def parse_conetnt(self,response):
        item = response.meta['item']
        content = response.xpath('//*[@id="content"]/div/div[2]/h1/text()').extract()[0]
        item['content'] = content
        yield item


    def parse(self, response):
        item = QiushiItem()
        li_lists = response.xpath('//*[@id="content"]/div/div[2]/div/ul/li')
        for li_list in li_lists:
            title = li_list.xpath('./div/a/text()').extract()[0]
            smile = li_list.xpath('./div/div/div/span[1]/text()').extract()[0]
            author = li_list.xpath('./div/div/a/span/text()').extract()[0]
            link = 'https://www.qiushibaike.com'+li_list.xpath('./a/@href').extract()[0]
            item['title'] = title
            item['smile'] = smile
            item['author'] = author
            item['link'] = link
            yield scrapy.Request(link,callback=self.parse_conetnt,meta={'item':item})
        for page in range(2,14):
            url = 'https://www.qiushibaike.com/8hr/page/'+str(page)
            yield scrapy.Request(url,callback=self.parse)


