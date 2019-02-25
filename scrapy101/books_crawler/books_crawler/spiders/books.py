# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']
    rules = (Rule(LinkExtractor(), callback = 'parse_page', follow = True),)
    
    def parse_page(self, response):
        yield({'url': response.url})
 