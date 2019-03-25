from scrapy.cmdline import execute

# 执行抓取
execute('scrapy crawl qidian'.split())

# 将结果输出
# execute('scrapy crawl qidian -o book.json'.split())