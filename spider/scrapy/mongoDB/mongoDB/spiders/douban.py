# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    """
    获取信息并保存到mongoDB中
    """
    name = 'douban111'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start={}&filter='.format(num * 25) for num in range(10)]

    def parse(self, response):
        titles = response.xpath('//span[@class="title"][1]/text()').extract()
        stars = response.xpath('//span[@class="rating_num"]/text()').extract()
        for title, star in zip(titles, stars):
            yield {
                "title": title,
                "star": star
            }
