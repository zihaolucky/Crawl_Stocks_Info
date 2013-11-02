# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.conf import settings
 
import codecs
 
 
#使用UTF-8格式保存文件
fp = codecs.open('record3.txt', 'w', 'utf-8')

class StockSpider3(BaseSpider):
    #设置爬虫名称
    name = "stocks3"
    #设置起始URL列表
    start_urls = ["http://quote.eastmoney.com/center/list.html#10"]
 
    
    def parse(self, response):
        req = []
        hxs = HtmlXPathSelector(response)
        #通过XPath选出公交车路线分类页面的URL
        result = []
        with open('/Users/white/crawler/stocks.csv','r') as f:
            for line in f:
                result = line.split('\r')
                #result.append((str,line.split('\r')))
            #print size(result)

        stock_urls = []
        for k in range(0,841):
            stock_urls.append("http://quote.eastmoney.com/sh"+result[k]+".html")
        print stock_urls
        
        
        print 'stock_urls =', stock_urls
        
        for url in stock_urls:
            #构建新的URL
            new_url = url
            print new_url
            print "[parse]new_url = %s" % (new_url)
            #创建对应的页面的Request对象，设定回调函数为parse_cat，利用parse_cat处理返回的页面
            r = Request(new_url, callback=self.parse_stocks)
            req.append(r)
        return req
        
        
    def parse_stocks(self, response):
        req = []
        hxs = HtmlXPathSelector(response)
        #通过XPath选出每一条公交路线的URL
        line_urls = hxs.select('//div[@id="gghylist"]/ul[1]//a/@href').extract()
        #catagory ? how to handle?
        #stocks = response.url.split('/')[-1]
        #print "stocks =", stocks
        #print "line_urls =", line_urls
        for url in line_urls:
            #构建新的URL
            new_url = url
            #print "[parse_stocks]new_url = %s" % (new_url)
            #创建对应的页面的Request对象，设定回调函数为parse_line，利用parse_line处理返回的页面
            r = Request(new_url, callback=self.parse_news)
            req.append(r)
        return req
 
    def parse_news(self, response):
        hxs = HtmlXPathSelector(response)
        #利用XPath抽取出线路名称:line_name
        time = hxs.select('//div[@class="newsContent"]//div[@class="Info"]/span[2]/text()').extract()
        title = hxs.select('//div[@class="newText new"]/h1/text()').extract()
        info = hxs.select('//div[@id="ContentBody"]//text()').extract()
        
        fp.write(title[0])
        fp.write(",")
        fp.write(time[0])
        fp.write("\n")
        for i in range(0,len(info)):
            fp.write(info[i])
        fp.write("\n\n")
        
        print "#####"
        print title[0]
        print "#####\n\n"