import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor
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
        extractor = LinkExtractor()
        links = extractor.extract_links(response)
        url = self.find_holy_url(links)
        if url:
            yield scrapy.Request(url=url,callback=self.parse_holychords)

    def find_holy_url(self, links):
        for link in links :
            if 'holychords.com' in link.url:
                return link.url


    def parse_holychords(self, response):
        print(''.join(response.xpath('//pre[@id="music_text"]').getall()).replace('<br>', '\n'))

process = CrawlerProcess()
process.crawl(GoogleSpider)
process.start()
