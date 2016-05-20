# -*- coding: utf-8 -*-
from scrapy.item import Item

from dirbot.spiders.model.dmoz.items import DMOZ_ITEMS
from dirbot.spiders.model.dw.items import DW_ITEMS
from dirbot.spiders.model.jd_com.babyCare.items import JDBC_ITEMS
from dirbot.spiders.model.jd_com.xiangZi.items import jdxiangzi_ITEMS
from dirbot.spiders.model.jd_com.naiFen.items import JDNF_ITEMS
from dirbot.spiders.model.quarks.items import QUARKS_ITEMS
from dirbot.spiders.model.jd_com.huaZhuang.items import JDHZ_ITEMS
from dirbot.spiders.model.jd_com.guoJu.items import JDGJ_ITEMS
from dirbot.spiders.model.jd_com.daoJu.items import JDDJ_ITEMS
from dirbot.spiders.model.jd_com.wenJu.items import JDWJ_ITEMS
from dirbot.spiders.model.jd_com.peiJian.items import JDPJ_ITEMS
from dirbot.spiders.model.jd_com.xie.items import jdxie_ITEMS
# tmall.com
from dirbot.spiders.model.tmall_com.naiFen.items import TMALL_NAIFEN_ITEMS

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

    # jd_com variables
    jdnf_root_nav = JDNF_ITEMS.root_nav
    jdnf_fenlie =JDNF_ITEMS.fenlie
    jdnf_fenglie2 = JDNF_ITEMS.fenglie2
    jdnf_product_intro = JDNF_ITEMS.product_intro
    jdnf_spec_n1 = JDNF_ITEMS.spec_n1
    jdnf_p_ad = JDNF_ITEMS.p_ad
    jdnf_jd_price = JDNF_ITEMS.jd_price
    jdnf_product_detail_1 = JDNF_ITEMS.product_detail_1
    jdnf_parameter2 = JDNF_ITEMS.parameter2
    jdnf_canshu = JDNF_ITEMS.canshu
    jdnf_promises = JDNF_ITEMS.promises
    jdnf_zhengpin = JDNF_ITEMS.zhengpin
    jdnf_comment = JDNF_ITEMS.comment

    # deutsche welle
    dw_title = DW_ITEMS.title
    dw_enclosure = DW_ITEMS.enclosure
    dw_link = DW_ITEMS.link
    dw_description = DW_ITEMS.description

    # add babyCare variables
    jdbc_root_nav =JDBC_ITEMS.root_nav
    jdbc_fenlie = JDBC_ITEMS.fenlie
    jdbc_fenglie2 = JDBC_ITEMS.fenglie2
    jdbc_product_intro = JDBC_ITEMS.product_intro
    jdbc_spec_n1 = JDBC_ITEMS.spec_n1
    jdbc_p_ad = JDBC_ITEMS.p_ad
    jdbc_jd_price = JDBC_ITEMS.jd_price
    jdbc_choose = JDBC_ITEMS.choose
    jdbc_choose2 =JDBC_ITEMS.choose2
    jdbc_product_detail_1 = JDBC_ITEMS.product_detail_1
    jdbc_parameter2 = JDBC_ITEMS.parameter2
    jdbc_canshu = JDBC_ITEMS.canshu
    jdbc_promises = JDBC_ITEMS.promises
    jdbc_zhengpin = JDBC_ITEMS.zhengpin
    jdbc_comment = JDBC_ITEMS.comment

    #add  xiangZi variables
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

    #add huaZhuang variables
    jdhz_root_nav = JDHZ_ITEMS.root_nav
    jdhz_fenlie = JDHZ_ITEMS.fenlie
    jdhz_fenglie2 = JDHZ_ITEMS.fenglie2
    jdhz_product_intro = JDHZ_ITEMS.product_intro
    jdhz_spec_n1 = JDHZ_ITEMS.spec_n1
    jdhz_p_ad =JDHZ_ITEMS.p_ad
    jdhz_jd_price = JDHZ_ITEMS.jd_price
    jdhz_product_detail_1 = JDHZ_ITEMS.product_detail_1
    jdhz_parameter2 = JDHZ_ITEMS.parameter2
    jdhz_canshu = JDHZ_ITEMS.canshu
    jdhz_promises = JDHZ_ITEMS.promises
    jdhz_zhengpin = JDHZ_ITEMS.zhengpin
    jdhz_comment = JDHZ_ITEMS.comment

    #add guoJu varianles
    jdgj_root_nav = JDGJ_ITEMS.root_nav
    jdgj_fenlie = JDGJ_ITEMS.fenlie
    jdgj_fenglie2 = JDGJ_ITEMS.fenglie2
    jdgj_product_intro = JDGJ_ITEMS.product_intro
    jdgj_spec_n1 = JDGJ_ITEMS.spec_n1
    jdgj_p_ad = JDGJ_ITEMS.p_ad
    jdgj_jd_price = JDGJ_ITEMS.jd_price
    jdgj_product_detail_1 = JDGJ_ITEMS.product_detail_1
    jdgj_parameter2 = JDGJ_ITEMS.parameter2
    jdgj_canshu = JDGJ_ITEMS.canshu
    jdgj_promises = JDGJ_ITEMS.promises
    jdgj_zhengpin = JDGJ_ITEMS.zhengpin
    jdgj_comment = JDGJ_ITEMS.comment

    # add daoJu varianles
    jddj_root_nav = JDDJ_ITEMS.root_nav
    jddj_fenlie = JDDJ_ITEMS.fenlie
    jddj_fenglie2 = JDDJ_ITEMS.fenglie2
    jddj_product_intro = JDDJ_ITEMS.product_intro
    jddj_spec_n1 = JDDJ_ITEMS.spec_n1
    jddj_p_ad = JDDJ_ITEMS.p_ad
    jddj_jd_price = JDDJ_ITEMS.jd_price
    jddj_product_detail_1 = JDDJ_ITEMS.product_detail_1
    jddj_parameter2 = JDDJ_ITEMS.parameter2
    jddj_canshu = JDDJ_ITEMS.canshu
    jddj_promises = JDDJ_ITEMS.promises
    jddj_zhengpin = JDDJ_ITEMS.zhengpin
    jddj_comment = JDDJ_ITEMS.comment

    # add wenJu varianles
    jdwj_root_nav = JDWJ_ITEMS.root_nav
    jdwj_fenlie = JDWJ_ITEMS.fenlie
    jdwj_fenglie2 = JDWJ_ITEMS.fenglie2
    jdwj_product_intro = JDWJ_ITEMS.product_intro
    jdwj_spec_n1 = JDWJ_ITEMS.spec_n1
    jdwj_p_ad = JDWJ_ITEMS.p_ad
    jdwj_jd_price = JDWJ_ITEMS.jd_price
    jdwj_product_detail_1 = JDWJ_ITEMS.product_detail_1
    jdwj_parameter2 = JDWJ_ITEMS.parameter2
    jdwj_canshu = JDWJ_ITEMS.canshu
    jdwj_promises = JDWJ_ITEMS.promises
    jdwj_zhengpin = JDWJ_ITEMS.zhengpin
    jdwj_comment = JDWJ_ITEMS.comment

    # add peiJian varianles
    jdpj_root_nav = JDPJ_ITEMS.root_nav
    jdpj_fenlie = JDPJ_ITEMS.fenlie
    jdpj_fenglie2 = JDPJ_ITEMS.fenglie2
    jdpj_product_intro = JDPJ_ITEMS.product_intro
    jdpj_spec_n1 = JDPJ_ITEMS.spec_n1
    jdpj_p_ad = JDPJ_ITEMS.p_ad
    jdpj_jd_price = JDPJ_ITEMS.jd_price
    jdpj_product_detail_1 = JDPJ_ITEMS.product_detail_1
    jdpj_parameter2 = JDPJ_ITEMS.parameter2
    jdpj_canshu = JDPJ_ITEMS.canshu
    jdpj_promises = JDPJ_ITEMS.promises
    jdpj_zhengpin = JDPJ_ITEMS.zhengpin
    jdpj_comment = JDPJ_ITEMS.comment

    # add xie varianles
    jdxie_root_nav = jdxie_ITEMS.root_nav
    jdxie_fenlie = jdxie_ITEMS.fenlie
    jdxie_fenglie2 = jdxie_ITEMS.fenglie2
    jdxie_product_intro = jdxie_ITEMS.product_intro
    jdxie_spec_n1 = jdxie_ITEMS.spec_n1
    jdxie_p_ad = jdxie_ITEMS.p_ad
    jdxie_jd_price = jdxie_ITEMS.jd_price
    jdxie_product_detail_1 = jdxie_ITEMS.product_detail_1
    jdxie_parameter2 = jdxie_ITEMS.parameter2
    jdxie_canshu = jdxie_ITEMS.canshu
    jdxie_promises = jdxie_ITEMS.promises
    jdxie_zhengpin = jdxie_ITEMS.zhengpin
    jdxie_comment = jdxie_ITEMS.comment


    # tmall
    # naiFen
    tmall_naifen_root_nav = TMALL_NAIFEN_ITEMS.root_nav

