# -*- coding: utf-8 -*-
import scrapy

from noticias.items import NoticiasItem


class TecnoblogSpider(scrapy.Spider):
    name = 'Tecnoblog'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['http://tecnoblog.net/']

    def parse(self, response):
        for article in response.css("article"):
            link    = article.css("div.texts h2 a::attr(href)").extract_first()
            title   = article.css("div.texts h2 a::text").extract_first()
            author  = article.css("div.texts div.info a::text").extract_first()

            notice = NoticiasItem(title=title, author=author, link=link);

            yield notice