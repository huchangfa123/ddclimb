# -*- coding: utf-8 -*-

# Scrapy settings for dangdang project

BOT_NAME = 'dangdang'

SPIDER_MODULES = ['dangdang.spiders']
NEWSPIDER_MODULE = 'dangdang.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
   'dangdang.pipelines.DangdangPipeline': 300,
}

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = "dangdang"
MONGODB_DOCNAME = "books"

# REDIS_HOST = '192.168.1.199'
# REDIS_PORT = 6379