# 仅供学习参考

***项目库中包含两个项目，一个是豆瓣爬虫，一个是微信性别识别***

### 基于Scrapy的豆瓣读书 (https://book.douban.com/) 全站爬虫：

> 豆瓣读书是国内信息最全，用户数量最大且最为活跃的读书网站

> 爬虫项目是针对豆瓣读书基本上的全站抓取（部分不重要的信息忽略），主要抓取的内容有：

>> * 1、书名

>> * 2、作者

>> * 3、出版社

>> * 4、出版年份

>> * 5、价格

>> * 6、豆瓣评分

>> * 7、评价人数



### 爬虫默认为深度优先的策略，基于book.douban.com域名的深度爬虫

> 爬虫入口页为豆瓣图书标签页(https://book.douban.com/tag/?view=type&icn=index-sorttags-all),根据入口标签，深度爬取每个标签下的子页，提取子页的信息后再判断子页中的下一页信息，直到子页中没有下一页为止。

> 由于豆瓣读书会检测ip访问频率，爬虫访问频率过高ip容易被封，返回403状态码

![ip被封显示](https://github.com/xiaohanxxx/Wechat-Recognition/blob/master/douban/%E7%88%AC%E8%99%AB%E9%94%99%E8%AF%AF.png)

#### 解决方法

> 通过修改Scrapy框架中间件的process_request函数随机更换ip地址，爬虫的ip池里有36个ip，每次爬取更换一个ip避免爬虫在爬取的过程中断。

> pipelines的作用主要是将爬虫爬取到的数据存入数据库


### 程序运行示例：

![程序运行](https://github.com/xiaohanxxx/Wechat-Recognition/blob/master/douban/%E7%A8%8B%E5%BA%8F%E8%BF%90%E8%A1%8C.gif)


### 数据库显示：

![数据库显示](https://github.com/xiaohanxxx/Wechat-Recognition/blob/master/douban/%E6%95%B0%E6%8D%AE%E5%BA%93%E6%98%BE%E7%A4%BA.gif)



### 提高爬虫效率的方法：

> 1、因为ip池中的ip都是免费ip，爬取的速度会较慢，这里可以通过购买高质量的ip接口提高爬虫效率

> 2、可以使用多线程提高爬虫效率，只要网速跟的上，处理好并发，可轻松达到千万级数据量

> 3、如果电脑性能卓越，网速也不错，可以使用分布式爬虫（没必要）
