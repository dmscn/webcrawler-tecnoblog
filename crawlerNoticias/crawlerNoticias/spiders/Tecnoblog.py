# -*- coding: utf-8 -*-
import scrapy

from crawlerNoticias.items import NoticiasItem


class TecnoblogSpider(scrapy.Spider):
    name = 'Tecnoblog'
    allowed_domains = ['tecnoblog.net']
    start_urls = ['http://tecnoblog.net/']

    def parse(self, response):
        for article in response.css("article"):
            link    = article.css("div.texts h2 a::attr(href)").extract_first()

            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        link    = response.url
        title   = response.css("title ::text").extract_first()
        author  = response.css("span.author ::text").extract_first()
        text    = "".join(response.css("div.entry ::text").extract())

        notice = NoticiasItem(title=title, author=author, text=text, link=link)

        yield notice
