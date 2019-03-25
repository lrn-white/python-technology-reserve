# -*- coding: utf-8 -*-
import scrapy

"""
BaiduSpider处理抓取的数据
Pipeline存储抓取到的数据
"""
class BaiduSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/rank/yuepiao']

    # 对输出结果进行操作
    def parse(self, response):
        # 获取结果中的书名，作者名
        booknames = response.xpath('//h4/a/text()').extract()
        authors = response.xpath('//p[@class="author"]/a[1]/text()').extract()

        book = []
        for bookname, author in zip(booknames, authors):
            # book.append({"bookname": bookname, "author": author})
            # 将数据传输到Pipeline中，只能推送dict，item对象
            yield {"bookname": bookname, "author": author}
        # return book
