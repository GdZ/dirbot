# -*- coding: utf-8 -*-
import scrapy
import scrapy.log as Log

class MYBB_FILTER():
    item = []
    arrays = []

    # old settings
    paars = [
        {'body', '//ul[@class="clearfix"]/li'},
        {'key', 'b/text()'},
        {'value', 'text()'},
        ## breadCrumbs
        {'breadCrumbs_a_text', '//'},
        {'breadCrumbs_a_href', '//'},
        {'breadCrumbs_a_title_text', '//'},
        {'breadCrumbs_a_title_href', '//'},
        {'breadCrumbs_div_ctx', '//'},
        ## titlecon clearfix
        {'titleconClearfix_div_img_alt', '//'},
        {'titleconClearfix_div_img_src', '//'},
        ## right l
        # div_pi_price_box
        {'div_rightl_pbox_price_span_i', '//'},
        {'div_rightl_pbox_price_span_em', '//'},
        {'div_rightl_pbox_price_span_pbox_off', '//'},
        {'div_rightl_pbox_price_span_pbox_market', '//'},
        {'div_rightl_pbox_price_span_del', '//'},
        # dl_i_youhui
        {'dl_i_youhui_dt_num_name', '//'},
        {'dl_i_youhui_dt_div_iyh_zeng_text', '//'},
        {'dl_i_youhui_dt_div_iyh_zeng_i_text', '//'},
        # color new_gg
        {'dl_color_new_gg_ul_li_color_list_item_a_text', '//'},
        {'dl_color_new_gg_ul_li_color_list_item_a_em_text', '//'},
        # color
        {'dl_color_dt_color_name_text', '//'},
        {'dl_color_dt_color_list_ul_li_color_list_item_a_title', '//'},
        # J_num_select
        {'dl_J_num_select_dt_num_name_text', '//'},
        {'dl_J_num_select_dt_num_box_em_id_buyAmount', '//'}
    ]

    def __init__(self, Selector):
        """
        get root string
        """
        Log.logger.debug("filter ist: %s", self.paars[0][1])
        sites = Selector.xpath(self.paars[0][1])
        for site in sites:
            """
            for paar in self.paars:
                self.item[paar[0]]= site.xpath(paar[1]).extract()
                self.arrays.append(self.item)
            """
            paar = self.paars[0]
            self.item[paar[0]] = site.xpath(paar[1]).extract()
            self.arrays.append(self.item)
