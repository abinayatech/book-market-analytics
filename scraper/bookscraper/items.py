import scrapy

class BookItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    upc = scrapy.Field()
    category = scrapy.Field()
    description = scrapy.Field()
