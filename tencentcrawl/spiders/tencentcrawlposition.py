# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider
from tencentcrawl.items import TencentcrawlItem


class TencentcrawlpositionSpider(RedisCrawlSpider):
	name = 'tencentcrawlposition'
	#allowed_domains = ['tencent.com']
	#start_urls = ['https://hr.tencent.com/position.php?&start=0#']
   

	redis_key = "tencentpositionspider:start_urls"
	# 动态域范围获取
	def __init__(self, *args, **kwargs):
	# Dynamically define the allowed domains list.
		domain = kwargs.pop('domain', '')
		self.allowed_domains = filter(None, domain.split(','))
		super(TencentcrawlpositionSpider, self).__init__(*args, **kwargs)
 
	pageLink_rule = LinkExtractor(allow=r'start=\d+') 
	rules = (
		Rule(pageLink_rule, callback='parse_page', follow=True),
	)

	def parse_page(self, response):
		for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
			item = TencentcrawlItem()
            #职位名称
			item['pName'] = each.xpath('./td[1]/a/text()').extract()[0]

            #职位链接
			item['pLink'] = each.xpath('./td[1]/a/@href').extract()[0]

            #职位类别
			if each.xpath('./td[2]/text()').extract():
				item['pType'] = each.xpath('./td[2]/text()').extract()[0]
			else:
				item['pType'] = "NULL"
            #招聘人数
			item['peopleNum'] = each.xpath('./td[3]/text()').extract()[0]

            #工作地点
			item['workArea'] = each.xpath('./td[4]/text()').extract()[0]

            #职位发布时间
			item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]

			

			yield item
