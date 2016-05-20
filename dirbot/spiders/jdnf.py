# -*- coding: utf-8 -*-
"""
this is for dmoz sites samples-testing
"""
from scrapy.selector import Selector
from scrapy.spiders import Spider

from dirbot.items import Website
from dirbot.spiders.model.jd_com.naiFen.rules import JDNF_RULES


class jdSpider(Spider):
    rules = JDNF_RULES()
    name = rules.name
    allowed_domains = rules.allowed_domains
    start_urls = rules.start_urls

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        # sites = sel.xpath('//ul[@class="directory-url"]/li')
        # sites = sel.xpath(self.rules.filters['root']['0'])
        bodies= sel.xpath(self.rules.filters['body']['0'])

        items = []

        # for body in bodies:
        body = bodies
        for body in bodies:
            item = Website()
            # item['name'] = site.xpath('a/text()').extract()
            # jd_root_nav
            item['jdnf_root_nav'] = body.xpath(self.rules.filters['root_nav']['0']).extract()
            ## this two need not to two variables, because 'jd_root_nav' is a array
            #item['jdnf_fenlie'] = body.xpath(self.rules.filters['fenlie']['0']).extract()
            #item['jdnf_fenglie2'] =body.xpath(self.rules.filters['fenglie2']['0']).extract()

            # jdnf_product_intro
            # item['jdnf_product_intro'] = body.xpath(self.rules.filters['product_intro']['0'])
            item['jdnf_spec_n1'] = body.xpath(self.rules.filters['spec_n1']['0']).extract()
            ## this rules'jdnf_p_ad' is right, but cannot select. I don't know why
            item['jdnf_p_ad'] = body.xpath(self.rules.filters['p_ad']['0']).extract()

            ## this rules'jdnf_jd_price' is right, but cannot select. I don't know why
            item['jdnf_jd_price'] = body.xpath(self.rules.filters['jd_price']['0']).extract()
            #item['jdnf_product_detail_1'] = body.xpath(self.rules.filters['product_detail_1']['0'])
            #item['jdnf_parameter2'] = body.xpath(self.rules.filters['parameter2']['0'])
            item['jdnf_canshu'] = body.xpath(self.rules.filters['canshu']['0']).extract()

            # jdnf_promises
            #item['jdnf_promises'] = body.xpath(self.rules.filters['promises']['0'])
            #item['jdnf_zhengpin'] = body.xpath(self.rules.filters['zhengpin']['0']).extract()

            # jdnf_comment, this is comment list
            #item['jdnf_comment'] = body.xpath(self.rules.filters['comment']['0'])

            # add to list items
            items.append(item)

        return items


def parse(self, response):
    filename = response.url.split("/")[-2]
    with open(filename, 'wb') as f:
        f.write(response.body)
