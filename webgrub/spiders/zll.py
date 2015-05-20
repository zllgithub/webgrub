# -*- coding: utf-8 -*-
'''
Created on 2015/5/20

@author: zhangliangliang
'''
import scrapy

class TaobaoSpider(scrapy.spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['http://detail.tmall.com/item.htm?'
        'spm=a230r.1.14.1.vzrhmf&id=44334055143&cm_id'
        '=140105335569ed55e27b&abbucket=19']

