# -*- coding: utf-8 -*-
import scrapy


class Login2Spider(scrapy.Spider):
    """
    通过cookie登录
    """
    name = 'login2'
    allowed_domains = ['sxt.cn']

    # start_urls = ['http://www.sxt.cn/index/user.html']
    def start_requests(self):
        cookie_str = "UM_distinctid=1699f67644b702-0ca9401fa2302f-9333061-1fa400-1699f67644c824; CNZZDATA1261969808=1313969307-1553154844-" \
                     "%7C1553154844; zg_did=%7B%22did%22%3A%20%221699f6764843f4-0f37495b20f2c8-9333061-1fa400-1699f676485a60%22%7D; " \
                     "PHPSESSID=23t8sa7dmfr4mahncp0tf6jml6; 53gid2=10768906105002; 53gid0=10768906105002; 53gid1=10768906105002; " \
                     "53revisit=1553157547510; 53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_land_page=http%253A%252F%252Fwww.sxt.cn%252F; " \
                     "kf_72085067_land_page_ok=1; visitor_type=old; 53kf_72085067_keyword=http%3A%2F%2Fwww.sxt.cn%2Findex.html; " \
                     "zg_c1e08f0fa5e3446d854919ffa754d07f=%7B%22sid%22%3A%201553157547147%2C%22updated%22%3A%201553158157015%2C%22info%22%3A%2" \
                     "01553157547154%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E8%AF%B8%E" \
                     "8%91%9Bio%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22" \
                     "%22%2C%22landHref%22%3A%20%22http%3A%2F%2Fwww.sxt.cn%2F%22%7D"
        # 将cookie转换成字典格式
        cookies = {}
        for cookie in cookie_str.split(";"):
            key, value = cookie.split("=")
            cookies[key.strip()] = value

        yield scrapy.Request('http://www.sxt.cn/index/user.html', callback=self.parse, cookies=cookies)

    def parse(self, response):
        print(response.text)
