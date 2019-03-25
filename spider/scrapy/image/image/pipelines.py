# -*- coding: utf-8 -*-
import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImagePipeline(object):
    def process_item(self, item, spider):
        return item


class ImageNamePipeline(ImagesPipeline):
    """
    自定义pipeline
    """

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={"title_name": item["title_name"]})

    def file_path(self, request, response=None, info=None):
        title_name = request.meta["title_name"].strip().replace("\r\n\t\t", "").replace("/", "_") + ".jpg"
        return title_name
