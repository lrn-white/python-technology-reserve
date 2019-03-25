# -*- coding: utf-8 -*-
import scrapy


class ZolSpider(scrapy.Spider):
    """
    获取图片
    """
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/bizhi/7412_91953_2.html']

    def parse(self, response):
        image_url = response.xpath('//img[@id="bigImg"]/@src').extract()
        title_name = response.xpath('string(//h3)').extract_first()

        yield {
            "image_urls": image_url,
            "title_name": title_name
        }

        next_url = response.xpath('//a[@id="pageNext"]/@href').extract_first()
        # 判断是否是最后一张
        if next_url.find(".html") != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
