# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QiushiPipeline:
    def __init__(self):
        self.client = MongoClient(host='localhost',port=27017)
        self.db = self.client['糗事百科']
        self.collections = self.db['详情']

    def process_item(self, item, spider):
        data = {
            'title':item['title'],
            'author': item['author'],
            'smile': item['smile'],
            # 'link': item['link'],
            'content': item['content'],
        }
        print(data)
        self.collections.insert(data)
        return item

    def close_spider(self):
        self.collections.close()
