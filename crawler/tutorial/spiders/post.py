# -*- coding: utf-8 -*-
import scrapy
import pandas as pd
import os
dirname = os.path.dirname(__file__)


class PostSpider(scrapy.Spider):
    name = 'post'
    allowed_domains = ['forums.comodo.com']
    posts_file =  os.path.join(dirname,"../../forums.csv")
    posts = pd.read_csv(posts_file)
    start_urls = [post for post in posts["link"]]
    def parse(self, response):
        for post in response.css("td[class='subject windowbg2']"):
            yield{
                "post_title": post.css("div span a::text").extract_first(),
                "post_link": post.css("div span a::attr('href')").extract(),
                "user": post.css("div p a::attr('href')").extract()
            }
        
        

