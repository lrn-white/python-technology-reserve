# -*- coding: utf-8 -*-
import scrapy


class BiqukeSpider(scrapy.Spider):
    """
    读取小说第一章的内容，然后依次点击下一章来获取内容
    """
    name = 'biquke'
    allowed_domains = ['biquke.com']
    start_urls = ['https://www.biquke.com/bq/0/362/42001.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        # 将列表转换为字符串
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace("    ", "\n").replace("＋笔趣阁", "") \
            .replace("Wｗｗ。Ｂｉｑｕｋｅ。Ｃｏｍ＋", "").replace("！笔趣阁", "").replace("ＷＷＷ．ＢＩＱＵＫＥ．ＣＯＭ", "") \
            .replace("％笔趣阁　www．biquke．com％", "")

        yield {
            "title": title,
            "content": content
        }

        # 切换到下一章的url
        next_url = response.xpath('//div[@class="bottem"]/a[4]/@href').extract_first()
        # 判断是否为最后一章，如果是则停止爬取
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
