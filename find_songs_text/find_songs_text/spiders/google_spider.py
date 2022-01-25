import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.response import open_in_browser


class GoogleSpider(scrapy.Spider):
    name = "google_spider"
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'LOG_LEVEL': 'DEBUG',
    }
    start_urls = [
        "https://www.google.com/search?q=ангел у трона твоего+holychords",
        "https://www.google.com/",
        "https://github.com/scrapy/scrapy/issues/1612"

    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url, callback=self.parse_page
            )

    def parse_page(self, response):
        print()
        return


process = CrawlerProcess()
process.crawl(GoogleSpider)
