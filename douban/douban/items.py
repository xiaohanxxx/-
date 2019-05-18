# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import scrapy


class DoubanItem(scrapy.Item):
    title = scrapy.Field() #书名
    author = scrapy.Field()#作者
    score = scrapy.Field() #评分
    evaluate = scrapy.Field()#评价数