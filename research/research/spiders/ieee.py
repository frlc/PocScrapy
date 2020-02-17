# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class IeeeSpider(CrawlSpider):
    name = 'ieee'
    allowed_domains = ['www.ieee.org/']
    start_urls = ['https://conferences.ieee.org/conferences_events/conferences/search?q=*']
    rules = (
        Rule = (LinkExtractor(allow='/conferences_events/conferences/search?q=*')),
        Rule = (
            LinkExtractor(
                allow='/conferences_events/conferences/conferencedetails')
                
                callback='parse_conference'
                )
        
        
    )
    
    def parse_conference(self, response):
        self.log(response.xpath("//title/text()").extract_first())