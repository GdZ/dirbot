# -*- coding: utf-8 -*-
"""
this is for dmoz sites samples-testing
"""

from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.spiders.model.dw.rules import DW_RULES
from dirbot.items import Website


class DwSpider(Spider):
    rules = DW_RULES()
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
        sites = sel.xpath(self.rules.filters['root']['0'])
        items = []

        for site in sites:
            item = Website()
            item['dw_title'] = site.xpath(self.rules.filters['title']['0']).extract()
            item['dw_link'] = site.xpath(self.rules.filters['link']['0']).extract()
            item['dw_description'] = site.xpath(self.rules.filters['description']['0']).extract()
            item['dw_enclosure'] = site.xpath(self.rules.filters['enclosure']['0']).extract()
            items.append(item)

        return items
