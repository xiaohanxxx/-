# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

def dbdouban():
    conn = pymysql.connect('localhost',user='root',passwd='123456',db='douban')
    return conn



class DoubanPipeline(object):
    def process_item(self, item, spider):
        dbObject = dbdouban()
        cursor = dbObject.cursor()
        sql = "INSERT IGNORE INTO douban_data(title,author,score,evaluate) VALUES ('%s','%s','%s','%s')"%(item['title'],item['author'],item['score'],item['evaluate'])
        cursor.execute(sql)
        dbObject.commit()

        return item
