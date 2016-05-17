# -*- coding: utf-8 -*-
"""
this is for dmoz sites samples-testing
"""

from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.spiders.model.quarks.rules import QUARKS_RULES
from dirbot.items import Website


class QuarksSpider(Spider):
    rules = QUARKS_RULES()
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
            item['quarks_title'] = site.xpath(self.rules.filters['title']['0']).extract()
            item['quarks_link'] = site.xpath(self.rules.filters['link']['0']).extract()
            item['quarks_description'] = site.xpath(self.rules.filters['description']['0'])\
                .re(self.rules.filters['description']['1'])
            # item['quarks_pubdate'] = site.xpath(self.rules.filters['pubDate']['0'])
            items.append(item)

        return items
