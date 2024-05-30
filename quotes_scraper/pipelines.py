# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json


class QuotesPipeline:
    def open_spider(self, spider):
        self.quotes = []

    def close_spider(self, spider):
        with open('quotes.json', 'w') as file:
            json.dump(self.quotes, file, indent=4)

    def process_item(self, item, spider):
        if item.get('type') == 'quote':
            self.quotes.append(item)
        return item
    
class AuthorsPipeline:
    def open_spider(self, spider):
        self.authors = []

    def close_spider(self, spider):
        with open('authors.json', 'w') as file:
            json.dump(self.authors, file, indent=4)

    def process_item(self, item, spider):
        if item.get('type') == 'author':
            self.authors.append(item)
        return item

