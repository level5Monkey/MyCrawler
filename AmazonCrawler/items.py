# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    asin = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    url = scrapy.Field()
    time = scrapy.Field()