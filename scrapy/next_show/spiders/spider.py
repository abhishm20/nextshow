# -*- coding: utf-8 -*-
import logging
import re

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from next_show.items import IMDbId


class IMDBSpider(CrawlSpider):
    name = 'imdb'
    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths='//*[@id="main"]/div/div/div[4]/div/a'
            ),
            process_links=lambda links: filter(lambda l: 'Next' in l.text, links),
            callback='parse_page',
            follow=True),
    )

    def __init__(self, start=None, end=None, *args, **kwargs):
        super(IMDBSpider, self).__init__(*args, **kwargs)
        self.start_year = int(start) if start else 1874
        self.end_year = int(end) if end else 2020

    # generate start_urls dynamically
    def start_requests(self):
        for year in range(self.start_year, self.end_year+1):
            url = 'http://www.imdb.com/search/title?release_date=%s' % str(year)
            yield scrapy.Request(url)

    def parse_page(self, response):
        try:
            for sel in response.xpath('//h3/a'):
                item = IMDbId()
                link = sel.xpath('@href').extract()
                link = re.findall("/.*/", link[0])[0]
                item['imdb_id'] = link[7:-1]
                yield item
        except Exception as e:
            logging.exception(str(e))

    # make sure that the dynamically generated start_urls are parsed as well
    parse_start_url = parse_page
