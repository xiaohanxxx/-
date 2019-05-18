# -*- coding: utf-8 -*-
import scrapy,time
from douban.items import DoubanItem

class DoubanBookSpider(scrapy.Spider):
    name = 'douban_book'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/tag/?view=type&icn=index-sorttags-all/']

    # def parse(self, response):
    #     for i in response.xpath('//*[@id="content"]/div/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[1]/a/@href').getall():#得到标签的url
    #         new_url = response.urljoin(i)#构造新的完整url
    #         time.sleep(1)
    #         # print(new_url)
    #         yield scrapy.Request(new_url,callback=self.sublist)

    # def sublist(self, response):
    #     for i in response.css('li.subject-item'):
    #         douban = DoubanItem()
    #         title = ''.join(i.xpath('.//h2/a/text()').getall()).replace('\n','')#转换成字符串并删除换行符
    #         title = title.replace(' ','')#图书名
    #         douban['title'] = title
    #         print(douban)
    #
    #         yield douban


        # next_url = response.xpath('.//span[@class="next"]/a/@href').extract_first()
        # if next_url:
        #     new_url = response.urljoin(next_url)
        #     print(new_url)
        #     yield scrapy.Request(new_url, callback=self.sublist)



    def parse(self, response):
        for i in response.xpath('.//table/tbody/tr/td/a/@href').getall():#得到标签的url
            new_url = response.urljoin(i)#构造新的完整url
            time.sleep(1)
            # print(new_url)
            yield scrapy.Request(new_url,callback=self.sublist)


    def sublist(self,response):
        for i in response.css('li.subject-item'):
            douban = DoubanItem()
            title = ''.join(i.xpath('.//h2/a/text()').getall()).replace('\n','')#转换成字符串并删除换行符
            title = title.replace(' ','')#图书名
            douban['title'] = title

            author = ''.join(i.xpath('.//div[@class="pub"]/text()').getall()).replace('\n','')
            author = author.replace(' ','')#作者+出版社+出版日期+价格
            douban['author'] = author

            score = ''.join(i.xpath('.//span[@class="rating_nums"]/text()').getall())#评分
            douban['score'] = score

            evaluate = ''.join(i.xpath('.//span[@class="pl"]/text()').getall()).replace('\n','')#评价人数
            evaluate = evaluate.replace(' ','')
            douban['evaluate'] = evaluate
            yield douban

        next_url = response.xpath('.//span[@class="next"]/a/@href').extract_first()
        if next_url:
            new_url = response.urljoin(next_url)
            print(new_url)
            yield scrapy.Request(new_url,callback=self.sublist)


