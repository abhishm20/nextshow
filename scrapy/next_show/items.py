# -*- coding: utf-8 -*-
import scrapy


class IMDbId(scrapy.Item):
    imdb_id = scrapy.Field()
    is_used = scrapy.Field()
    created_at = scrapy.Field()
