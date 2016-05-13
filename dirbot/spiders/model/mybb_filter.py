# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector

from dirbot.spiders.mybb_task import LOG

class MYBB_FILTER():
    item = []
    arrays = []
    selector = Selector()

    # old settings
    rules = [
        {'0':'body', '1':'//ul[@class="clearfix"]/li'},
        {'0':'key', '1':'b/text()'},
        {'0':'value', '1':'text()'},
        ## breadCrumbs
        {'0':'breadCrumbs_a_text', '1':'//'},
        {'0':'breadCrumbs_a_href', '1':'//'},
        {'0':'breadCrumbs_a_title_text', '1':'//'},
        {'0':'breadCrumbs_a_title_href', '1':'//'},
        {'0':'breadCrumbs_div_ctx', '1':'//'},
        ## titlecon clearfix
        {'0':'titleconClearfix_div_img_alt', '1':'//'},
        {'0':'titleconClearfix_div_img_src', '1':'//'},
        ## right l
        # div_pi_price_box
        {'0':'div_rightl_pbox_price_span_i', '1':'//'},
        {'0':'div_rightl_pbox_price_span_em', '1':'//'},
        {'0':'div_rightl_pbox_price_span_pbox_off', '1':'//'},
        {'0':'div_rightl_pbox_price_span_pbox_market', '1':'//'},
        {'0':'div_rightl_pbox_price_span_del', '1':'//'},
        # dl_i_youhui
        {'0':'dl_i_youhui_dt_num_name', '1':'//'},
        {'0':'dl_i_youhui_dt_div_iyh_zeng_text', '1':'//'},
        {'0':'dl_i_youhui_dt_div_iyh_zeng_i_text', '1':'//'},
        # color new_gg
        {'0':'dl_color_new_gg_ul_li_color_list_item_a_text', '1':'//'},
        {'0':'dl_color_new_gg_ul_li_color_list_item_a_em_text', '1':'//'},
        # color
        {'0':'dl_color_dt_color_name_text', '1':'//'},
        {'0':'dl_color_dt_color_list_ul_li_color_list_item_a_title', '1':'//'},
        # J_num_select
        {'0':'dl_J_num_select_dt_num_name_text', '1':'//'},
        {'0':'dl_J_num_select_dt_num_box_em_id_buyAmount', '1':'//'}
    ]

    def __init__(self, Selector):
        """
        get root string
        """
        LOG.debug(self.__class__ + "->__init__ begin")
        self.selector = Selector
        LOG.debug(self.__class__ + "->__init__ end")

    def run(self):
        LOG.debug(self.__class__ + "->run() begin")
        rule_item = self.rules[0]['1']
        sites = self.selector.xpath(rule_item)
        LOG.debug("self.rules[0]=" + rule_item)
        for site in sites:
            """
            for paar in self.paars:
                self.item[paar[0]]= site.xpath(paar[1]).extract()
                self.arrays.append(self.item)
            """
            paar = self.rules[0]
            LOG.logger.debug("%s")
            self.item[paar[0]] = site.xpath(paar[1]).extract()
            self.arrays.append(self.item)
        LOG.debug(self.__class__ + "->run() end")
