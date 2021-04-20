# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


def list_strip(itens):
    if len(itens) > 0:
        return itens[0]
    else:
        return None


class PhonebotItem(scrapy.Item):
    logo = scrapy.Field(
        output_processor=list_strip
    )
    phones = scrapy.Field()
    website = scrapy.Field(
        output_processor=list_strip
    )

