# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

import itemadapter
from itemadapter import ItemAdapter


class ProductScraperPipeline:

    def __init__(self):
        self.file = None

    def open_spider(self, spider):
        self.file = open('product.txt', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        print(adapter.get('name'))
        self.file.write(json.dumps(adapter.asdict()) + '\n')
        return item
