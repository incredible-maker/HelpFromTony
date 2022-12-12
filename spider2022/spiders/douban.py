import scrapy
from scrapy import Selector

from spider2022.items import MovieItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        sel = Selector(response)
        list_items = sel.css('#content > div > div.article > ol > li')
        for i in list_items:
            movie_items = MovieItem()
            movie_items['title'] = i.css('span.title::text').extract_first
            movie_items['rank'] = i.css('span.rating_num::text').extract_first
            movie_items['quote'] = i.css('span.inq::text').extract_first
            yield movie_items.get()

