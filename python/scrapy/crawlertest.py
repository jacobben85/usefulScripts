import scrapy


class MySpider(scrapy.Spider):
    name = 'uvn bot'
    allowed_domains = ['univision.com']
    start_urls = [
        'http://www.univision.com/',
    ]

    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)

        for url in response.xpath('//a/@href').extract():
            if 'univision.com' in url:
                yield scrapy.Request(url, callback=self.parse)