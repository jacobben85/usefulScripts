# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import UnivisionItem


class UnivisionSpider(scrapy.Spider):
    handle_httpstatus_list = range(400, 427) + range(500, 511)
    name = "univision"
    allowed_domains = ["univision.com"]
    start_urls = (
        'http://www.univision.com/',
    )

    def parse(self, response):

        item = UnivisionItem()
        item['status'] = response.status
        item['link'] = response.url
        item['referer'] = response.request.headers.get('Referer', None)
        yield item

        if response.status is 200:
            for url in response.xpath('//a/@href').extract():
                if 'univision.com' in url:
                    yield scrapy.Request(url, callback=self.parse)
        else:
            print response.status
            print response