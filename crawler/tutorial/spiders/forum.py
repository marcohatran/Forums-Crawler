# -*- coding: utf-8 -*-
import scrapy

class MalwareSpider(scrapy.Spider):
    name = 'forum'
    allowed_domains = ['forums.comodo.com']
    start_urls = ['https://forums.comodo.com/?af=9557']

    def parse(self, response):
        for content in response.css("td[class='info']"):
            yield{
                "title": content.css("a[class='subject']::text").extract_first(),
                "description": content.css("p ::text").extract(),
                "link": content.css("a[class='subject']::attr('href')").extract()
            }

