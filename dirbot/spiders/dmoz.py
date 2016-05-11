# -*- coding: utf-8 -*-
"""
this is for dmoz sites samples-testing
"""
from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.spiders.model.dmoz_items import DMOZ_ITEMS
from dirbot.spiders.model.dmoz_rules import DMOZ_RULES
from dirbot.items import Website

class DmozSpider(Spider):
    rules = DMOZ_RULES()
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
            # item['name'] = site.xpath('a/text()').extract()
            item['name'] = site.xpath(self.rules.filters['name']['0']).extract()
            item['url'] = site.xpath(self.rules.filters['url']['0']).extract()
            item['description'] = site.xpath(self.rules.filters['description']['0'])\
                .re(self.rules.filters['description']['1'])
            items.append(item)

        return items
