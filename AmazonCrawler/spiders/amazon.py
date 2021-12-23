import scrapy
from datetime import datetime

class AmazonCrawler(scrapy.Spider):
    name = "AmazonCrawler"
        
    def start_requests(self):
        url = 'https://www.amazon.ca/s?k='
        keyword = getattr(self, 'keyword', None)
        if keyword is not None:
            url = url + keyword
        yield scrapy.Request(url, self.parse)
        
    def parse(self, response):
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        keyword = getattr(self, 'keyword', None)
        
        for product in response.xpath("//*[@data-asin]"):
            asin = product.xpath("./@data-asin").get()
            title = product.xpath(".//h2/a/span/text()").get()
            price = product.xpath(".//a/span[@class='a-price']/span[@class='a-offscreen']/text()").get()
            image = product.xpath(".//img[@class='s-image']/@src").get()
            url = 'https://www.amazon.ca' + product.xpath(".//h2/a/@href").get() if product.xpath(".//h2/a/@href").get() else None
            if asin is not None and title is not None and price is not None and image is not None and url is not None and keyword.upper() in title.upper():
                yield {
                    'keyword': keyword,
                    'time': time,
                    'asin': asin,
                    'title': title,
                    'price': price,
                    'image': image,
                    'url': url,
                }
