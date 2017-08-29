# -*- coding: utf-8 -*-

# Scrapy settings for befrank project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

DB_NAME = 'imdb_ids.db'

BOT_NAME = 'next_show'

SPIDER_MODULES = ['next_show.spiders']
NEWSPIDER_MODULE = 'next_show.spiders'

DOWNLOAD_DELAY = 5
CONCURRENT_REQUESTS = 250

ITEM_PIPELINES = {
    'next_show.pipelines.Pipeline': 0
}

DOWNLOAD_TIMEOUT = 180

LOG_FILE = "scrapy.log"
# LOG_ENABLED = False
# LOG_LEVEL = 'WARNING'
