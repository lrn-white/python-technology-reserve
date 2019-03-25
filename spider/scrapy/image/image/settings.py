# -*- coding: utf-8 -*-

BOT_NAME = 'image'

SPIDER_MODULES = ['image.spiders']
NEWSPIDER_MODULE = 'image.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    # 自定义
    'image.pipelines.ImageNamePipeline': 300
    # 官方的
    # 'scrapy.pipelines.images.ImagesPipeline': 300
}
IMAGES_STORE = '../images'
