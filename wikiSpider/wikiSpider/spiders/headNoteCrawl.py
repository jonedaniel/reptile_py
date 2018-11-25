import scrapy

from wikiSpider.items import HeadNote

tiebaName = ""
aim = ""

def urlGen():
    L = []
    base_str = "http://tieba.baidu.com/f?kw="+tiebaName+"&ie=utf-8&pn="
    for i in range(0, 2000):
        L.append(base_str + (i * 50).__str__())
    return L

class HeadNoteCrawl(scrapy.Spider):


    name = "headNote"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = urlGen()

    def parse(self, response):
        item = HeadNote()
        for sel in response.xpath('//div[@class="threadlist_lz clearfix"]'):
            theme = sel.xpath('div/a[@class="j_th_tit "]/text()').extract()
            no_icon_author = sel.xpath('div/span[@class="tb_icon_author no_icon_author"]/@title').extract()
            icon_author = sel.xpath('div/span[@class="tb_icon_author "]/@title').extract()
            href = sel.xpath('div/a[@class="j_th_tit "]/@href').extract()
            author = no_icon_author if len(no_icon_author)>0 else icon_author
            if aim in "".join(author):
                print(href)
        return item

