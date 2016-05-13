# -*- coding: utf-8 -*-
"""
scrapy import
"""
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector
from dirbot.spiders.action.mybb_action import MYBB_ACTION

import logging as LOG

class MYBB_SPIDER(Spider):
    """
    class define.
    global variables define
    """
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

        selector = Selector(response)
        LOG.debug("create filter ........")
        action = MYBB_ACTION()
        # action.run()

        return action.items
