# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.conf import settings
 
import codecs
 
 
#使用UTF-8格式保存文件
fp = codecs.open('record2.txt', 'w', 'utf-8')

class StockSpider2(BaseSpider):
    #设置爬虫名称
    name = "stocks2"
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
            r = Request(new_url, callback=self.parse_info)
            req.append(r)
        return req
 
    def parse_info(self, response):
        hxs = HtmlXPathSelector(response)
        #利用XPath抽取出线路名称:line_name
        stock_name = hxs.select('/html/body/div["qbox"]/div["qmain"]/div["rol"]/div["base"]/div["tit"]/div["coll"]/a/h1/text()').extract()
        print 'stock name =',stock_name[0]
        print ''
        #利用XPath抽取路线中经过的站点名称:route
        a = hxs.select('/html/body/div["qbox"]/div["qmain"]/div["rcol"]/div["qmbox"]/div["mlbox"]/div["gsjjsj"]/table//td["vds"]/text()').extract()
        info = [a[1],a[3],a[5],a[6],a[7],a[8],a[10],a[11],a[12],a[14],a[16],a[18]]
        
        #结果写入到记录的文件之中
        fp.write(stock_name[0].strip())
        fp.write('\r\n')
        opt = ''
        #每个站点之间用|隔开
        for name in info:
            opt += (name.strip() + ',')
        opt = opt[:-1]
        fp.write(opt)
        fp.write('\r\n')
        print "#####"
        print stock_name[0].strip()
        print opt
        print "#####"