# -*- coding: utf-8 -*-
import scrapy
from douban.items import MovieItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # 解析页面
        li_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for li in li_list:

            item = MovieItem()
            # 电影名字，肖申克救赎
            item['movie'] = li.xpath('div/div[2]/div[1]/a/span[1]/text()').extract_first()
            # 评分， 9.6
            item['rate'] = li.xpath('div/div[2]/div[2]/div/span[2]/text()').extract_first()
            # 说明，'希望让人自由'
            item['motto'] = li.xpath('div/div[2]/div[2]/p[2]/span/text()').extract_first()
            yield item
        # 带href的 a 标签, ::attr("href")即取出属性是href--超链接
        href_list = response.css('a[href]::attr("href")').re('\?start=.*')
        for href in href_list:
            # 将超链接补完整
            url = response.urljoin(href)
            # 返回request 对象,给一个新的url，处理完url还是执行parse方法
            yield scrapy.Request(url=url, callback=self.parse)
