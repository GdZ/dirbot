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
        'root_nav': {'0':'/div', '1':''},
        # yiji fen lie
        'fenlie': {'0':'a/text()', '1':''},
        # erji fenglei
        'fenglie2': {'0': 'a/text()', '1': ''},

        # 1. product-intro
        'product_intro': {'0':'div/@id="product-intro"', '1': ''},
        # 1.1. Product title
        'spec_n1': {'0': 'div/div/@alt', '1':''},
        'p_ad': {'0': 'div[@id="p-ad"]/text()', '1': ''},
        # 1.2 price
        'jd_price': {'0':'div[@id="jd-price"]/text()', '1': ''},

        # 2 Product deteials 1
        'product_detail_1': {'0': 'div[@id="product-detail-1"]', '1': ''},
        # 2.1 Chanpimncanshu *13
        'parameter2': {'0': 'div[@id="parameter2"]', '1': ''},
        'canshu': {'0': 'li/@title', '1': ''},

        ###'': {'0':'', '1':''},
        # 3. promises
        'promises': {'0': 'div[@id="promises"]', '1': ''},
        # 3.1 zhengpin
        'zhengpin': {'0': 'dd/text()', '1': ''},
        # 4.  comment
        'comment': {'0':'div[id="comment"]', '1':''},



        #### to be continue.....
    }
