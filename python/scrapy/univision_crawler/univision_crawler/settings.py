# -*- coding: utf-8 -*-

# Scrapy settings for univision_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import sys
import MySQLdb

BOT_NAME = 'univision_crawler'

SPIDER_MODULES = ['univision_crawler.spiders']
NEWSPIDER_MODULE = 'univision_crawler.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'univision_crawler (+http://www.yourdomain.com)'

USER_AGENT = '%s' % (BOT_NAME)

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