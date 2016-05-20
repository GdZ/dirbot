# -*- coding: utf-8 -*-
from scrapy.item import Item

from dirbot.spiders.model.dmoz.items import DMOZ_ITEMS
from dirbot.spiders.model.dw.items import DW_ITEMS
from dirbot.spiders.model.jd.jdbc.items import jdbc_ITEMS
from dirbot.spiders.model.jd.jdxiangzi.items import jdxiangzi_ITEMS
from dirbot.spiders.model.jd.milch.items import jd_ITEMS
from dirbot.spiders.model.quarks.items import QUARKS_ITEMS


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
    jd_root_nav = jd_ITEMS.root_nav
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

    # deutsche welle
    dw_title = DW_ITEMS.title
    dw_enclosure = DW_ITEMS.enclosure
    dw_link = DW_ITEMS.link
    dw_description = DW_ITEMS.description

    # add jdbc variables
    jdbc_root_nav =jdbc_ITEMS.root_nav
    jdbc_fenlie = jdbc_ITEMS.fenlie
    jdbc_fenglie2 = jdbc_ITEMS.fenglie2
    jdbc_product_intro = jdbc_ITEMS.product_intro
    jdbc_spec_n1 = jdbc_ITEMS.spec_n1
    jdbc_p_ad = jd_ITEMS.p_ad
    jdbc_jd_price = jdbc_ITEMS.jd_price
    jdbc_choose = jdbc_ITEMS.choose
    jdbc_choose2 =jdbc_ITEMS.choose2
    jdbc_product_detail_1 = jdbc_ITEMS.product_detail_1
    jdbc_parameter2 = jdbc_ITEMS.parameter2
    jdbc_canshu = jdbc_ITEMS.canshu
    jdbc_promises = jdbc_ITEMS.promises
    jdbc_zhengpin = jdbc_ITEMS.zhengpin
    jdbc_comment = jdbc_ITEMS.comment

    #add  jdxiangzi variables
    jdxiangzi_root_nav = jdxiangzi_ITEMS.root_nav
    jdxiangzi_fenlie = jdxiangzi_ITEMS.fenlie
    jdxiangzi_fenglie2 = jdxiangzi_ITEMS.fenglie2
    jdxiangzi_product_intro = jdxiangzi_ITEMS.product_intro
    jdxiangzi_spec_n1 = jdxiangzi_ITEMS.spec_n1
    jdxiangzi_p_ad = jdxiangzi_ITEMS.p_ad
    jdxiangzi_jd_price = jdxiangzi_ITEMS.jd_price
    jdxiangzi_product_detail_1 = jdxiangzi_ITEMS.product_detail_1
    jdxiangzi_parameter2 = jdxiangzi_ITEMS.parameter2
    jdxiangzi_canshu = jdxiangzi_ITEMS.canshu
    jdxiangzi_promises = jdxiangzi_ITEMS.promises
    jdxiangzi_zhengpin = jdxiangzi_ITEMS.zhengpin
    jdxiangzi_comment = jdxiangzi_ITEMS.comment

