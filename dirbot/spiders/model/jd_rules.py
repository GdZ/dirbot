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
        # 'root': {'0': '//ul[@class="p-parameter"]/li', '1': ''},
        # alles infomationen
        'boby': {'0': '//boby', '1':''},
        # root-nav
        'root-nav': {'0':'', '1':''},
        # 1. product-intro
        'product-intro': {'0':'div/@id="product-intro"', '1':''},
        # 1.1. spec-nl
        'spec-n1': {'0':'', '1':''},
        '': {'0':'', '1':''},
        # 2.
        '': {'0':'', '1':''},
        '': {'0':'', '1':''},
        # 3.
        '': {'0':'', '1':''},
        '': {'0':'', '1':''},
        'pname': {'0':'li/@title()', '1':''},
        'pID': {'0':'li/@title()', '1': ''},
        'bName': {'0':'li/@title()', '1': ''},

        #### to be continue.....
    }
