import scrapy
from univision_crawler.items import UnivisionCrawlerItem


class UnivisionSpider(scrapy.Spider):
    name = 'UnivisionSpider'
    allowed_domains = ['www.univision.com']
    start_urls = [
        'http://www.univision.com/',
    ]

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)

        for title in response.xpath('//title').extract():
            yield UnivisionCrawlerItem(item_title=title)

        for url in response.xpath('//a/@href').extract():
            if 'www.univision.com' in url:
                yield scrapy.Request(url, callback=self.parse)