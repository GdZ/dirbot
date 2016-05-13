# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class jd_RULES():
    name = "jd"
    allowed_domains = ["www.jd.com"]
    start_urls = [
        "https://item.jd.com/1279473.html",
        "https: // item.jd.com / 1216716.html"

    ]
    filters = {
      ## 'root': {'0':'//ul[@class="directory-url"]/li', '1': ''},
        'root': {'0': '//ul[@class="p-parameter"]/li', '1': ''},
        'pname': {'0':'li/@title()', '1':''},
        'pID': {'0':'li/@title()', '1': ''},
        'bName': {'0':'li/@title()', '1': ''},

        #### to be continue.....
    }
