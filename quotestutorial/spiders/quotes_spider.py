import scrapy
from ..items import QuotestutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        boxes = response.xpath('//div[@class="quote"]')

        items = QuotestutorialItem()
        for box in boxes:
            quotes = box.xpath('.//span[@class="text"]/text()').extract()
            author = box.xpath('.//small[@class="author"]/text()').extract()
            
            items['quotes'] = ''.join(quotes)
            items['author'] = ''.join(author)
            
            yield items