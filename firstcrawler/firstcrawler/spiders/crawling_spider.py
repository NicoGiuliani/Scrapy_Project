from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "primaryspider"
    allowed_domains = ["toscrape.com"]
    start_urls = ["http://books.toscrape.com/"]

    rules = (
        Rule(LinkExtractor(allow="catalogue/category/books"), callback="parse_item"),
        # Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"),
    )

    def parse_item(self, response):
        title_and_price = dict(
            zip(
                response.css(".product_pod a::attr(title)").getall(),
                response.css(".price_color::text").getall(),
            )
        )

        yield {
            "category": response.css(".page-header h1::text").get(),
            "number_results": response.css(".form-horizontal strong::text").get(),
            "title_and_price": title_and_price,
        }
