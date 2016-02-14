# -*- coding: utf-8 -*-
import scrapy


class DomainSpider(scrapy.Spider):
    name = "domain"
    allowed_domains = ["domain.com.au"]
    start_urls = (
        'http://www.domain.com.au/',
    )

    def parse(self, response):
        print(response.body)
        #pass
