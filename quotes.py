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
        yield{
            'auther_name':response.css('small.author').extract(),
            'text':response.css('span.text::text').extract_first(),
            'tags':response.css('a.tag::text').extract(),
        }
        
        # now run spider again by usig scrapy runspider quotes.py
        ## we can save data in json  scrapy runspider -o items.json
