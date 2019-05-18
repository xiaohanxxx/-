# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random


class DoubanSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DoubanDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        thisip = random.choice(self.IPPOOL)
        print("this is ip:"+thisip["http"])
        request.meta["proxy"] = "http://" + thisip["http"]

    IPPOOL = [
    {'http': '120.236.130.132:8060'},
    {'http': '117.191.11.77: 80'},
    {'http': '118.190.95.35: 9001'},
    {'http': '114.67.235.233: 3128'},
    {'http': '221.178.176.25: 3128'},
    {'http': '159.89.141.36: 8080'},
    {'http': '94.242.59.135: 1448'},
    {'http': '217.23.69.146: 8080'},
    {'http': '201.217.209.39: 3128'},
    {'http': '103.89.253.246: 3128'},
    {'http': '110.74.221.169: 59124'},
    {'http': '197.216.2.11: 8080'},
    {'http': '113.53.91.214: 8080'},
    {'http': '168.228.51.238: 8080'},
    {'http': '159.65.13.98: 8080'},
    {'http': '24.227.222.204: 53281'},
    {'http': '217.10.45.103: 8081'},
    {'http': '202.124.42.147: 8080'},
    {'http': '138.122.51.87: 3128'},
    {'http': '46.151.192.170: 42429'},
    {'http': '190.15.193.6: 8080'},
    {'http': '36.66.98.6: 53281'},
    {'http': '78.31.0.27: 8080'},
    {'http': '103.56.232.130: 31816'},
    {'http': '122.146.68.17: 8080'},
    {'http': '182.23.107.210: 3128'},
    {'http': '178.219.123.73: 8080'},
    {'http': '192.140.29.218: 60514'},
    {'http': '113.53.228.95: 80'},
    {'http': '117.191.11.112: 8080'},
    {'http': '103.42.213.176: 8080'},
    {'http': '104.248.7.62: 8080'},
    {'http': '210.212.31.215: 8080'},
    {'http': '203.189.142.23: 53281'},
    {'http': '82.222.50.195: 9090'},
    {'http': '183.81.157.182: 8080'},
    {'http': '106.75.212.158: 8080'},
    ]
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called


    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
