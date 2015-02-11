import scrapy


class MySpider(scrapy.Spider):
    name = 'pgs bot'
    allowed_domains = ['www.preetigowrisanthanam.com']
    start_urls = [
        'http://www.preetigowrisanthanam.com/',
        'http://www.preetigowrisanthanam.com/blog/',
    ]

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)

        for url in response.xpath('//a/@href').extract():
            if 'www.preetigowrisanthanam.com' in url:
                yield scrapy.Request(url, callback=self.parse)