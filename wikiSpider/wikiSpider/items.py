# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Article(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()


class HeadNote(scrapy.Item):
    note = scrapy.Field()

class YouNote(scrapy.Item):
    createdTime = scrapy.Field()
    theme = scrapy.Field()
    reply = scrapy.Field()
