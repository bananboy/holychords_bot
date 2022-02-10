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

    def parse_page(self, response):
        extractor = LinkExtractor()
        links = extractor.extract_links(response)
        url = self.find_holy_url(links)
        if url:
            yield scrapy.Request(url=url, callback=self.parse_holychords)

    def find_holy_url(self, links):
        for link in links:
            if 'holychords.com' in link.url:
                return link.url

    def parse_holychords(self, response):
        song_name = response.xpath('//h1/text()').get()
        song_text = ''.join(response.xpath('//pre[@id="music_text"]/text()').getall()).replace('<br>', '\n')
        yield {'song_name': song_name, 'song_text': song_text}


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(GoogleSpider)
    process.start()
