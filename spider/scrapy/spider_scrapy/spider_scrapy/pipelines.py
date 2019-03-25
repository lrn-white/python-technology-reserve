# -*- coding: utf-8 -*-

import json
from typing import TextIO


class SpiderScrapyPipeline(object):
    """
    接受并输出数据
    """

    # 抓取开始前打开文件
    def open_spider(self, spider):
        self.filename = open('book.txt', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        # 字典转换为字符串
        self.filename.write(json.dumps(item, ensure_ascii=False) + "\n")
        return item

    # 抓取完成后关闭文件
    def close_spider(self, spider):
        self.filename.close()
