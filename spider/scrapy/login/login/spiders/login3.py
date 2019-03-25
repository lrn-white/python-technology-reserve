# -*- coding: utf-8 -*-
import scrapy
import re


class Login3Spider(scrapy.Spider):
    """
    复杂formdata，带验证码及其他参数
    username: 17764591796
    password: 123456
    setcookie: 14
    checkCode:
    next: /
    source: passport
    __hash__: AK2/11GUHDHuSzuCgZloHFhEM8vzJw4gzeUOJZCmE08WdC8VC+d7jX9jXUijr3rH
    """
    name = 'login3'
    allowed_domains = ['ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']

    def parse(self, response):
        hash_code = re.search(r'"__hash__":"(.+)"', response.text)[0]
        # 获取验证码图片
        img_url = response.xpath('//img[@class="login-img-checkcode"]/@src').extract_first()
        yield scrapy.Request(img_url, callback=self.parse_info, meta={"hash_code": hash_code})

    def parse_info(self, response):
        with open("验证码.jpg", "wb") as f:
            f.write(response.body)
        code = input("请输入验证码：")
        form_data = {
            "username": "17764591796",
            "password": "123456asd",
            "setcookie": "14",
            "checkCode": code,
            "next": "/",
            "source": "passport",
            "__hash__": response.request.meta["hash_code"]
        }
        login_url = "https://passport.ganji.com/login.php"
        yield scrapy.FormRequest(login_url, formdata=form_data, callback=self.after_login)

    def after_login(self, response):
        print(response.text)
