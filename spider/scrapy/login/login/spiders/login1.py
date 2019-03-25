# -*- coding: utf-8 -*-
import scrapy


class Login1Spider(scrapy.Spider):
    """
    登录演示,通过账号密码登录
    """
    name = 'login1'
    allowed_domains = ['sxt.cn']

    # start_urls = ['http://www.sxt.cn/index/login/login.html']
    def start_requests(self):
        url = 'http://www.sxt.cn/index/login/login.html'
        form_data = {
            "user": "17764591796",
            "password": "123456"
        }
        yield scrapy.FormRequest(url, formdata=form_data, callback=self.parse)

    def parse(self, response):
        yield scrapy.Request("http://www.sxt.cn/index/user.html", callback=self.parse_info)

    def parse_info(self, response):
        print(response.text)
