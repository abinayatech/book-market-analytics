import scrapy
from bookscraper.items import BookItem

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    def parse(self, response):
        # Iterate over all books on the current page
        books = response.css('article.product_pod')
        for book in books:
            book_url = book.css('h3 a::attr(href)').get()
            # Follow the link to the book detail page
            yield response.follow(book_url, callback=self.parse_book_detail)

        # Handle pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_book_detail(self, response):
        item = BookItem()
        
        # Primary info
        item['title'] = response.css('.product_main h1::text').get()
        item['price'] = response.css('.product_main p.price_color::text').get()
        
        # Rating is in a class name like "star-rating Three"
        rating_classes = response.css('.product_main p.star-rating::attr(class)').get()
        if rating_classes:
            item['rating'] = rating_classes.split()[-1] # Gets "Three"
            
        # Product Description
        # It's usually the p tag after the product_description div, but structure varies.
        # Safest is to look for the id description and get the next sibling p
        item['description'] = response.xpath('//div[@id="product_description"]/following-sibling::p/text()').get()
        
        # Product Information Table check
        rows = response.css('table.table-striped tr')
        for row in rows:
            header = row.css('th::text').get()
            value = row.css('td::text').get()
            if header == 'UPC':
                item['upc'] = value
            elif header == 'Product Type':
                item['category'] = value # Sometimes category is here, but better from breadcrumb
        
        # Breadcrumb for Category (better source)
        # 3rd li in breadcrumb usually: Home -> Books -> Category -> Title
        categories = response.css('ul.breadcrumb li a::text').getall()
        if len(categories) >= 3:
            item['category'] = categories[2]
            
        yield item
