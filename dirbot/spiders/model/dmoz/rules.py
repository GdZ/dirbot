# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class DMOZ_RULES():
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
    ]
    filters = {
        'root': {'0':'//ul[@class="directory-url"]/li', '1': ''},
        'name': {'0':'a/text()', '1':''},
        'description': {'0':'text()', '1': '-\s[^\n]*\\r'},
        'url': {'0':'a/@href', '1': ''},
    }
