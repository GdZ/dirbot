# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class QUARKS_RULES():
    name = "quarks"
    allowed_domains = ["podcast.wdr.de"]
    start_urls = [
        "http://podcast.wdr.de/quarks.xml",
    ]

    filters = {
        'root': {'0':'//channel/item', '1':''},
        'title': {'0':'title/text()', '1':''},
        'link': {'0':'link/text()', '1':''},
        'description': {'0':'description/text()', '1':'-\s[^\n]*\\r'},
        'pubDate': {'0':'pubDate/text()', '1':''},
    }
