# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        #print the log 
        self.log('i just visited'+ response.url)
        # run this commmand in consol 
        #scrapy runspider file_name(quotes.py)
        # make dictionary and get data
        for quote in response.css('div.quote'):
            item={
                'auther_name':quote.css('small.author').extract(),
                'text':quote.css('span.text::text').extract_first(),
                'tags':quote.css('a.tag::text').extract(),
            }
            yield(item)
        
        # now run spider again by usig scrapy runspider quotes.py
        ## we can save data in json  scrapy runspider -o items.json
