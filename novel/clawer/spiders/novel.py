# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from clawer.items import ClawerItem


class MovieSpider(CrawlSpider):
    name = 'novel'
    allowed_domains = ['www.biquge.com.tw']
    start_urls = ['http://www.biquge.com.tw/']
    rules = (
        Rule(LinkExtractor(allow=(r'http://www.biquge.com.tw/[a-z]+/$'))),
        Rule(LinkExtractor(allow=(r'http://www.biquge.com.tw/\d+_\d+/$')), ),
        Rule(LinkExtractor(allow=(r'http://www.biquge.com.tw/\d+_\d+/\d+.html$')), callback='parse_item'),
    )

    def parse_item(self, response):
        sel = Selector(response)
        item = ClawerItem()

        item['name'] = sel.xpath('//div[@class="bookname"]/div/a[3]/text()').extract_first()
        item['author'] = sel.xpath('//*[@id="newscontent"]/div[1]/ul/li[1]/span[3]/text()').extract()
        item['total'] = sel.xpath('//*[@id="wrapper"]/div[4]/div/div[1]/a[2]/text()').extract()
        contents = response.xpath('//*[@id="content"]/text()')
        s = ''
        for content in contents:
            if len(content.re('\S+')) > 0:
                s += content.re('\S+')[0]
        item['content'] = s
        return item





