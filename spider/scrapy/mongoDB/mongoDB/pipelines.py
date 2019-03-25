# -*- coding: utf-8 -*-

import pymongo


class MongodbPipeline(object):

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("localhost", 27017)

    def process_item(self, item, spider):
        self.client.douban.movie.insert_one(item)
        return item

    def close_spider(self, spider):
        self.client.close()
