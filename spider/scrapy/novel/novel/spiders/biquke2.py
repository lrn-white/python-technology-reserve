# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

"""
scrapy genspider -t crawl biquke2 biquke.com

crawlspider框架演示
"""


class Biquke2Spider(CrawlSpider):
    name = 'biquke2'
    allowed_domains = ['biquke.com']
    start_urls = ['https://www.biquke.com/bq/0/362/']

    rules = (
        # 注意：要单独获取第一章
        Rule(LinkExtractor(restrict_xpaths='//dl/dd[1]/a'), callback='parse_item', follow=True),
        # restrict_xpaths：下一章跳转的url，提取下一章内容
        Rule(LinkExtractor(restrict_xpaths='//div[@class="bottem"]/a[4]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.xpath('//h1/text()').extract_first()
        # 将列表转换为字符串
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace("    ", "\n").replace("＋笔趣阁", "") \
            .replace("Wｗｗ。Ｂｉｑｕｋｅ。Ｃｏｍ＋", "").replace("！笔趣阁", "").replace("ＷＷＷ．ＢＩＱＵＫＥ．ＣＯＭ", "") \
            .replace("％笔趣阁　www．biquke．com％", "")

        yield {
            "title": title,
            "content": content
        }
