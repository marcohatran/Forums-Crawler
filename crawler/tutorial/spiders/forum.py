# -*- coding: utf-8 -*-
import scrapy

class MalwareSpider(scrapy.Spider):
    name = 'forum'
    allowed_domains = ['f319.com']
    start_urls = ['http://f319.com/']

    def parse(self, response):
        for content in response.css("td[class='info']"):
            yield{
                "title": content.css("a[class='subject']::text").extract_first(),
                "description": content.css("p ::text").extract(),
                "link": content.css("a[class='subject']::attr('href')").extract()
            }

