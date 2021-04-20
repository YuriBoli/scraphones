import scrapy
from scrapy.loader import ItemLoader
from phonebot.items import PhonebotItem
import sys
import logging
from .utils import phone_filter
from .utils import logo_filter


class PhoneNumbersSpider(scrapy.Spider):
    """
    Finds logo and phone numbers from sites :v
    """
    name = 'phonenumber'
    custom_settings = {
        'FEEDS': {
            'phonenumbers.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': True,
                'fields': ['logo', 'phones', 'website'],
                'item_export_kwargs': {
                    'export_empty_fields': True,
                },
            },
        }
    }

    def start_requests(self, *args, **kwargs):
        # get urls from file or input
        for url in sys.stdin:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        """
        Generates, fills and loads PhonebotItem
        :return:loaded PhonebotItem
        """
        item = ItemLoader(item=PhonebotItem(), response=response)
        item.add_value('phones', phone_filter(response))
        item.add_value('logo', logo_filter(response))
        item.add_value('website', response.url)
        return item.load_item()
