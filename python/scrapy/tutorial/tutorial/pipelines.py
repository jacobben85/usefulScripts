# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from settings import CONN

class UnivisionPipeline(object):
    def process_item(self, item, spider):
        CUR=CONN.cursor()

        link    = item['link']
        status  = item['status']
        referer = item['referer']

        link    = (link[:250] + '..') if len(link) > 253 else link

        if referer is not None:
            referer = (referer[:250] + '..') if len(referer) > 253 else referer

        CUR.execute("INSERT into univision (link, status, referer) VALUES (%s, %s, %s)", (link, status, referer))
        spider.log("INSERT into univision (link, status, referer) VALUES (%s, %s, %s)" % (link, status, referer))
        CONN.commit()
        return item
