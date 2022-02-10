# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from datetime import datetime
from scrapy.exceptions import DropItem


class CheckItemPipeline:
    '''
    checks for missing items in received data
    '''
    def process_item(self, article, spider):
        '''
        checkes for missing items and removes the whole object if any of the
        items are missing
        '''
        if not article['lastUpdated'] or not article['url'] or not article['title']:
            raise DropItem('Missing something!')
        return article


class CleanDatePipeline:
    '''
    Changes the date for last updated to a python datetime object
    '''
    def proces_item(self, article, spider):
        '''
        removes the text from the date and changes it into python date time object
        '''
        article['lastUpdated'].replace('This page was last edited on', '').strip()
        article['lastUpdated'] = datetime.strptime(article['lastUpdated'], '%d %B %Y, at %H:%M')
        return article
