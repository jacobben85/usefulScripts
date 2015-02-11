# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import UnivisionItem


class UnivisionSpider(scrapy.Spider):
    name = "univision"
    allowed_domains = ["www.univision.com"]
    start_urls = (
        'http://www.univision.com/',
    )

    def parse(self, response):

        for title in response.xpath('//title'):
            item = UnivisionItem()
            item['title'] = title.xpath('text()').extract()
            item['link'] = response.url
            yield item

        for url in response.xpath('//a/@href').extract():
            if 'www.univision.com' in url:
                yield scrapy.Request(url, callback=self.parse)