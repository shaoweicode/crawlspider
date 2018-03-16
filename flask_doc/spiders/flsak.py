# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem
import re
class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = "http://flask.pocoo.org/docs/0.12/"
    # http://flask.pocoo.org/docs/0.12/
    rules = (
        Rule(LinkExtractor(allow=('flask.pocoo.org/docs/0.12/', )), callback='parse_item',follow=True),
    )

    def parse_page(self, response):
        item = PageItem()
        """
        TODO:补充 url 和 text 的解析规则
        """
        item['url'] = response.url
        item['text']= response.css('div.section::text').extract_first()

        yield item