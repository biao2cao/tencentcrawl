# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
	pName = scrapy.Field()
	pLink = scrapy.Field()
	pType = scrapy.Field()
	peopleNum = scrapy.Field()
	workArea = scrapy.Field()
	publishTime = scrapy.Field()
	# utc 时间
	time = scrapy.Field()
    # 爬虫名
	spidername = scrapy.Field()
