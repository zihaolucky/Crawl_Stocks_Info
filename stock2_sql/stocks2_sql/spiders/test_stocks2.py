# -*- coding: utf-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.conf import settings
 
import codecs
import sqlite3 
 
#使用UTF-8格式保存文件
fp = codecs.open('record2_sql.txt', 'w', 'utf-8')

#配置/初始化数据库stock.db
cx = sqlite3.connect("/Users/white/stock.db")
cu = cx.cursor()
#create table 创建表
cu.execute("create table basic_info (symbol char,start_time datetime,gental_capital text,circulation_stock text,EPS text,NAVPS text,ROE text,revenue text,revenue_growth_rate text,sale_profit_rate text,net_profit text,NPGR text,undistributed_profit text)")

class StockSpider2(BaseSpider):
    #设置爬虫名称
    name = "stocks2_sql"
    #设置起始URL列表
    start_urls = ["http://quote.eastmoney.com/center/list.html#10"]
 
    
    def parse(self, response):
        req = []
        hxs = HtmlXPathSelector(response)
        #通过XPath选出页面的URL
        result = []
        #记得修改stocks.csv的路径!
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
            #创建对应的页面的Request对象，设定回调函数为parse_info，处理返回的页面
            r = Request(new_url, callback=self.parse_info)
            req.append(r)
        return req
 
    def parse_info(self, response):
        hxs = HtmlXPathSelector(response)
        #利用XPath抽取出股票名称:stock_name
        stock_name = hxs.select('/html/body/div["qbox"]/div["qmain"]/div["rol"]/div["base"]/div["tit"]/div["coll"]/a/h1/text()').extract()
        print 'stock name =',stock_name[0]
        print ''
        #利用XPath抽取股票信息:info
        a = hxs.select('/html/body/div["qbox"]/div["qmain"]/div["rcol"]/div["qmbox"]/div["mlbox"]/div["gsjjsj"]/table//td["vds"]/text()').extract()
        info = [stock_name[0],a[1],a[3],a[5],a[6],a[7],a[8],a[10],a[11],a[12],a[14],a[16],a[18]]
        
        #结果写入到记录的文件之中
        opt = ''
        #每个信息之间用,隔开
        for name in info:
            opt += (name.strip() + ',')
        opt = opt[:-1]
        fp.write(opt)
        fp.write('\r\n')
        print "#####"
        print opt
        print "#####"
        
        #insert into sqlite3 database.
        cx.execute("insert into basic_info values(?,?,?,?,?,?,?,?,?,?,?,?,?)", info)
        cx.commit()