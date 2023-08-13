# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ProjetoGloboItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    newspaper_section = scrapy.Field()
    subtitle = scrapy.Field()
    pass
