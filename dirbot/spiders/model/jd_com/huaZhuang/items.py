# -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class JDHZ_ITEMS():
    root_nav = Field()
    fenlie = Field()
    fenglie2 = Field()
    product_intro = Field()
    spec_n1 = Field()
    p_ad = Field()
    jd_price = Field()
    # added new
    choose = Field()
    choose2 = Field()
    #
    product_detail_1 = Field()
    parameter2 = Field()
    canshu = Field()
    promises = Field()
    zhengpin = Field()
    comment = Field()
    comment_num = Field()
