# -*- coding: utf-8 -*-
import scrapy
from scrapy.item import Item, Field

from dirbot.spiders.model.dmoz_items import DMOZ_ITEMS
from dirbot.spiders.model.quarks_items import QUARKS_ITEMS
from dirbot.spiders.model.jd_items import jd_ITEMS


class Website(Item):
    # dmoz variables
    dmoz_name = DMOZ_ITEMS.name
    dmoz_description = DMOZ_ITEMS.description
    dmoz_url = DMOZ_ITEMS.url

    # quarks variables
    quarks_title = QUARKS_ITEMS.title
    quarks_link = QUARKS_ITEMS.link
    quarks_description = QUARKS_ITEMS.description
    quarks_pubdate = QUARKS_ITEMS.pubDate

    # jd variables

    jd_root_nav =jd_ITEMS.root_nav
    jd_fenlie =jd_ITEMS.fenlie
    jd_fenglie2 = jd_ITEMS.fenglie2
    jd_product_intro = jd_ITEMS.product_intro
    jd_spec_n1 = jd_ITEMS.spec_n1
    jd_p_ad = jd_ITEMS.p_ad
    jd_jd_price = jd_ITEMS.jd_price
    jd_product_detail_1 = jd_ITEMS.product_detail_1
    jd_parameter2 = jd_ITEMS.parameter2
    jd_canshu = jd_ITEMS.canshu
    jd_promises = jd_ITEMS.promises
    jd_zhengpin = jd_ITEMS.zhengpin
    jd_comment = jd_ITEMS.comment



