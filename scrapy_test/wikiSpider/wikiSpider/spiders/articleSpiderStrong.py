from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from wikiSpider.items import Article


class ArticleSpiderStrong(CrawlSpider):
    name = "article2"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Python"]
    rules = [Rule(LinkExtractor(allow=('(/wiki/)((?!:).)*$'), ), callback="parse_item", follow=True)]

    def parse_item(self,response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is:"+title)
        item['title'] = title
        return item