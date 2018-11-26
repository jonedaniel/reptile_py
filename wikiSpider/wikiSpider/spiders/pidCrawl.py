from wikiSpider.items import YouNote
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor

tiebaName = ''

def urlGen():
    L = []
    base_str = "http://tieba.baidu.com/f?kw="+tiebaName+"&ie=utf-8&pn="
    for i in range(0, 2000):
        L.append(base_str + (i * 50).__str__())
    return L

class NoteCrawl(CrawlSpider):
    name = "pid"
    start_urls = urlGen()
    rules = [Rule(LinkExtractor('(/p/)'),callback="parse_item")]

    def parse_item(self, response):
        item = YouNote()
        for sel in response.xpath('//div[@class="l_post j_l_post l_post_bright  "]'):
            author = sel.xpath('div[@class="d_author"]/ul[@class="p_author"]/li[@class="d_name"]/@data-field').extract()
            if pid in "".join(author):
                title = response.xpath('/html/head/title/text()').extract()
                reply = sel.xpath('div[@class="d_post_content_main"]//div[@class="d_post_content j_d_post_content  clearfix"]/text()').extract()
                print("".join(title) + ":" + "".join(author) + " : " + "".join(reply))
        return item