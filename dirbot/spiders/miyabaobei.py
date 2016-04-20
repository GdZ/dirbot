# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website



class MybbSpider(Spider):
    name = "mybb"
    allowed_domains = ["miyabaobei.hk"]
    start_urls = [
        "http://www.miyabaobei.hk/item-1076411.html"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="clearfix"]/li')
        items = []

        for site in sites:
            item = Website()
            # item['name'] = site.xpath('a/text()').extract()
            # item['url'] = site.xpath('a/@href').extract()
            # item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            item['key'] = site.xpath('b/text()').extract()
            item['value'] = site.xpath('text()').extract()
            items.append(item)

        return items
