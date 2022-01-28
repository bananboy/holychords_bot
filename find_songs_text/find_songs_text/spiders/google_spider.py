import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.response import open_in_browser as view


class GoogleSpider(scrapy.Spider):
    name = "google_spider"
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'LOG_LEVEL': 'DEBUG',
    }
    start_urls = [
        "https://www.google.com/search?q=ангел у трона твоего+holychords",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url, callback=self.parse_page
            )

    def parse_page(self, response):
        href = response.xpath('//*[@id="main"]/div[4]/div/div[1]/a/@href').get()
        full_url = href.split('=', 1)[1]
        clear_url = full_url.split('&', 1)[0]
        yield scrapy.Request(url=clear_url,callback=self.parse_holychords)

    def parse_holychords(self, response):
        return

process = CrawlerProcess()
process.crawl(GoogleSpider)
process.start()
