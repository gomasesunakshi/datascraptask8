import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        titles = response.css('h3 a::attr(title)').getall ()
        for i in titles:
            yield {
                'title': i
            }
   


