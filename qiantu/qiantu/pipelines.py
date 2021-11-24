# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline

class imagesPipelines(ImagesPipeline):
    def get_media_requests(self,item,info):

        # 这个方法是在发送下载请求之前调用的，其实这个方法本身就是去发送下载请求的
        yield scrapy.Request(item['link'])

    def file_path(self,request,response=None,info=None):
        ImageName = request.url.split('/')[-1]
        return ImageName

    def item_completed(self,results,item,info ):
        return item