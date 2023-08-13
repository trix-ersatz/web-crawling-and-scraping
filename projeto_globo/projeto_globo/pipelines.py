# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json


class ProjetoGloboPipeline:
    def open_spider(self, spider):
        self.file = open('notices.json', 'w')
        self.items = []

    def close_spider(self, spider):
        json.dump(self.items, self.file, indent=4)
        self.file.close()

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item