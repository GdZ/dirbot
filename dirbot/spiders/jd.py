# -*- coding: utf-8 -*-
"""
this is for dmoz sites samples-testing
"""
from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.spiders.model.jd_rules import jd_RULES
from dirbot.items import Website

class jdSpider(Spider):
    rules = jd_RULES()
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
        item = Website()
        # item['name'] = site.xpath('a/text()').extract()
        item['jd_root_nav'] = body.xpath(self.rules.filters['root_nav']['0']).extract()
        item['jd_fenlie'] = body.xpath(self.rules.filters['fenlie']['0']).extract()
        item['jd_fenglie2'] =body.xpath(self.rules.filters['fenglie2']['0']).extract()
        item['jd_root_nav'] = body.xpath(self.rules.filters['root_nav']['0']).extract()
        item['jd_fenlie'] = body.xpath(self.rules.filters['fenlie']['0']).extract()
        item['jd_fenglie2'] = body.xpath(self.rules.filters['fenglie2']['0']).extract()
        item['jd_product_intro'] = body.xpath(self.rules.filters['product_intro']['0']).extract()
        item['jd_spec_n1'] = body.xpath(self.rules.filters['spec_n1']['0']).extract()
        item['jd_p_ad'] = body.xpath(self.rules.filters['p_ad']['0']).extract()
        item['jd_jd_price'] = body.xpath(self.rules.filters['jd_price']['0']).extract()
        item['jd_product_detail_1'] = body.xpath(self.rules.filters['product_detail_1']['0']).extract()
        item['jd_parameter2'] = body.xpath(self.rules.filters['parameter2']['0']).extract()
        item['jd_canshu'] = body.xpath(self.rules.filters['canshu']['0']).extract()
        item['jd_promises'] = body.xpath(self.rules.filters['promises']['0']).extract()
        item['jd_zhengpin'] = body.xpath(self.rules.filters['zhengpin']['0']).extract()
        item['jd_comment'] = body.xpath(self.rules.filters['comment']['0']).extract()

        items.append(item)


        return items


def parse(self, response):
    filename = response.url.split("/")[-2]
    with open(filename, 'wb') as f:
        f.write(response.body)