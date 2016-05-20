# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

class jdbc_RULES():
    name = "jdbc"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://item.jd.com/1765933470.html"
    ]
    filters = {
        # 'root': {'0': '//ul[@class="p-parameter"]/li', '1': ''},
        # alles infomationen
        'body': {'0': '//body', '1':''},
        # root-nav -ok
        'root_nav': {'0':'//div[@id="root-nav"]/div/div/*/a/text()', '1':''},
        # output maybe brandnam,e
        'fenlie': {'0':'a/text()', '1':''},
        # erji fenglei
        'fenglie2': {'0': 'a/text()', '1': ''},
        # 1. product-intro
        'product_intro': {'0':'//div[@id="product-intro"]', '1': ''},
        # 1.1. Product title
        'spec_n1': {'0': '//div[@id="spec-n1"]/img/@src', '1':''},
        #promotiion information
        'p_ad': {'0': '//div[@id="p-ad"]/text()', '1': ''},
        # 1.2 price
        'jd_price': {'0':'//strong[@id="jd-price"]/text()', '1': ''},
        # choose product variables
        'choose': {'0': '//div[@id="choose"]/div/div/*/a/text()', '1': ''},
        'choose2': {'0': '//div[@class="item"]/*/a/text()', '1': ''},
        # 2 Product deteials 1
        'product_detail_1': {'0': '//div[@id="product-detail-1"]', '1': ''},
        # 2.1 Chanpimncanshu *13
        'parameter2': {'0': '//ul[@id="parameter2"]', '1': ''},
        'canshu': {'0': '//ul[@id="parameter2"]/li/@title', '1': ''},
        # 3. promises
        'promises': {'0': '//div[@id="promises"]/text()', '1': ''},
        # 4. comment
        'comment': {'0': '//div[@id="comments-list"]', '1':''},
        'comment_num': {'0': '//div[@id="comments-list"]/div/div/ul/li'},

        # 5. product_detail_2

        #### to be continue.....
    }
