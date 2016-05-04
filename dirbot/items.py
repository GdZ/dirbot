from scrapy.item import Item, Field


class Website(Item):

    # name = Field()
    # description = Field()
    # url = Field()
    ## breadCrumbs
    breadCrumbs_a_ctx = Field()
    breadCrumbs_a_href = Field()
    breadCrumbs_a_title_ctx = Field()
    breadCrumbs_a_title_href = Field()
    breadCrumbs_div_ctx = Field()

    ## titlecon clearfix
    titleconClearfix_div_img_alt = Field()
    titleconClearfix_div_img_src = Field()

    ## right l
    # div_pi_price_box
    div_rightl_pbox_price_span_i = Field()
    div_rightl_pbox_price_span_em = Field()
    div_rightl_pbox_price_span_pbox_off = Field()
    div_rightl_pbox_price_span_pbox_market = Field()
    div_rightl_pbox_price_span_del = Field()
    # dl_i_youhui
    dl_i_youhui_dt_num_name = Field()
    dl_i_youhui_dt_div_iyh_zeng_text = Field()
    dl_i_youhui_dt_div_iyh_zeng_i_text = Field()
    # color new_gg
    dl_color_new_gg_ul_li_color_list_item_a_text = Field()
    dl_color_new_gg_ul_li_color_list_item_a_em_text = Field()
    # color
    dl_color_dt_color_name_text = Field()
    dl_color_dt_color_list_ul_li_color_list_item_a_title = Field()
    # J_num_select
    dl_J_num_select_dt_num_name_text = Field()
    dl_J_num_select_dt_num_box_em_id_buyAmount = Field()

    ## big rel
    key = Field()
    value = Field()
