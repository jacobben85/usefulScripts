# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import MySQLdb

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

ITEM_PIPELINES = [
    'tutorial.pipelines.UnivisionPipeline',
]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

# SQL DATABASE SETTING
SQL_DB = 'scrapy'
SQL_TABLE = 'univision'
SQL_HOST = 'localhost'
SQL_USER = 'jbjohn'
SQL_PASSWD = 'jbjohn'

# connect to the MySQL server
try:
    CONN = MySQLdb.connect(host=SQL_HOST,
                         user=SQL_USER,
                         passwd=SQL_PASSWD,
                         db=SQL_DB)
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)