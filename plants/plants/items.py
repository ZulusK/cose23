# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PostItem(scrapy.Item):
    """
        define item structure post at forum
    """
    author_id = scrapy.Field()
    author_name=scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    url = scrapy.Field()
    topic_id = scrapy.Field()
