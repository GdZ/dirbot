# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
from dirbot.spiders.model.filter import MYBB_FILTER as mybb_filter

from dirbot.items import Website

class MybbSpider(Spider):
    name = "mybb"
    allowed_domains = ["miyabaobei.hk"]
    start_urls = [
        "http://www.miyabaobei.hk/item-1076411.html"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        items = mybb_filter(sel).items

        return items
