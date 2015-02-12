# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from settings import CONN

class UnivisionPipeline(object):
    def process_item(self, item, spider):
        CUR=CONN.cursor()
        CUR.execute("INSERT into univision (link, status, referer) VALUES (%s, %s, %s)", (item['link'], item['status'], item['referer']))
        spider.log("INSERT into univision (link, status, referer) VALUES (%s, %s, %s)" % (item['link'], item['status'], item['referer']))
        CONN.commit()
        return item
