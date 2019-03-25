from lxml import etree
import requests

"""
xpath：一门从html中提取数据的语言
xpathhelper：帮助我们从elements中定位数据
1.选择节点（标签):'/html/head/meta','//li',‘//div[@class='home-top']’，'//div/@class','//div/text()'
"""

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Refer": "https://movie.douban.com/explore"
}

response = requests.get(url, headers=headers)
html_str = response.content.decode()

# 使用etree处理数据
html = etree.HTML(html_str)

# 获取所有电影图片的url地址
url_list = html.xpath("//div[@class='list']//a/@href")
