# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class GuaziSpider(scrapy.Spider):
    name = 'guazi2'
    allowed_domains = ['guazi.com']

    # start_urls = ['https://www.guazi.com/shaoxing/buy/']

    def start_requests(self):
        lua = '''
            function main(splash, args)
              assert(splash:go(args.url))
              assert(splash:wait(1))
              return splash:html()
            end
        '''
        yield SplashRequest("https://www.guazi.com/bj/buy/", callback=self.parse, endpoint='execute',
                            args={'lua_source': lua})

    def parse(self, response):
        print(response.text)
