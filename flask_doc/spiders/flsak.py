# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from flask_doc.items import PageItem

class FlaskSpider(scrapy.spiders.CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = "http://flask.pocoo.org/docs/0.12/"

    rules = (
        Rule("TODO: 配置 Link Extractor，及爬取链接的规则，并合理定义其他相关参数"),
    )

    def parse_page(self, response):
        item = PageItem()
        """
        TODO:补充 url 和 text 的解析规则
        """
        yield item