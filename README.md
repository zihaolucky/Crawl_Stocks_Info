Crawl_Stocks_Info
=================
这是一个基于Python Scrapy的爬虫.属于我学年论文(如果导师允许的话)的一个部分。路漫漫其修远兮,然光阴似箭,时不我待.


##### stocks2    
 `stocks2` 系列主要用于抓取上市公司股票的主要信息。在股票基本信息方面，目前包括“上市日期”、“市盈率”、“总市值”、“流通市值”等数据；其中又分为 `sql` 版和 `nosql` 版，牵着会将抓取结果存入 sqlite3，后者建立文本文档来储存数据。抓取速度尚可。




##### stocks3    
 `stocks3` 从“东方财富网”上抓取公司新闻。事实上，新闻数据是用于做文本分析和挖掘的。我希望可以通过分词、关键词提取等方式，结合社会网络方法，将各个上市公司看作一个网络中的节点，建立起上市公司的Social Network


#### How to do? Do it yourself!    
Scrapy的学习并不非常困难。事实上，我并没有完全按照tutorial的说法去写我的爬虫，而是先模仿别人的代码，先对整个架构的核心有一个了解和认识。这个核心，在我看来，便是spider下的主文件。

剩下的，包括如何存储(txt,sql)的问题，我没有采用Scrapy自带的pipline方法。而是去学习了Python调用sqlite3的方法，最后的效果还不错。不过，可能pipline的方法更快。

总之...写代码就是要动手，先思考再动手。加油吧！



##### Notes:     
 `1.` 目前能力有限，在关键词提取上有很大困难。若用传统方法做提取，与人脑判别有较大出入。还望与有兴趣相投的同学老师一起学习~

 `2.` 大家可以进入具体的文件夹，如 `stocks2_sql` 的页面，那里有具体一些的文档。希望能帮到大家！

##### About Me    
    Zihao Zheng    
    School of Mathematics    
    South China Normal University    
    Mail: zihaolucky@gmail.com


