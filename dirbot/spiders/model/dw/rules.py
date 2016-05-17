# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class DW_RULES():
    name = "dw"
    allowed_domains = ["rss.dw.com"]
    start_urls = [
        "http://rss.dw.com/xml/DKpodcast_topthemamitvokabeln_de",
    ]

    filters = {
        'root': {'0':'//channel/item', '1':''},
        'title': {'0':'title/text()', '1':''},
        'link': {'0':'link/text()', '1':''},
        'description': {'0':'description/text()', '1':'-\s[^\n]*\\r'},
        'enclosure': {'0':'enclosure/@url', '1':''},
    }
