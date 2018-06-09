# -*- coding: utf-8 -*-
import re
from urllib.parse import urlencode
import scrapy
from taobao.items import GoodsItem
from io import StringIO


class TaobaSpider(scrapy.Spider):
    name = 'taoba'
    allowed_domains = ['www.taobao.com']
    start_urls = ['http://www.taobao.com/']

    def start_requests(self):
        base_url = 'https://s.taobao.com/search?'
        params = {}
        for keyword in ['ipad', 'iphone', '小米手机']:
            params['q'] = keyword
            for page in range(10):
                params['s'] = page * 44
                full_url = base_url + urlencode(params)
                yield scrapy.Request(url=full_url, callback=self.parse)

    def parse(self, response):
        good_list = response.xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]')
        for goods in good_list:
            item = GoodsItem()
            item['price'] = goods.xpath('div[5]/div[2]/div[1]/div[1]/strong/text()').extract_first()
            item['deal'] = goods.xpath('div[5]/div[2]/div[1]/div[2]/text()').extract_first()
            segments = goods.xpath('div[6]/div[2]/div[2]/a/text()').extract()
            title = StringIO()
            for segment in segments:
                title.write(re.sub('\s', '', segment))
                item['title'] = title.getvalue()

            yield item
