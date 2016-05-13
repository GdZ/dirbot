# -*- coding: utf-8 -*-

from scrapy.item import Item

from dirbot.spiders.model.dmoz.items import DMOZ_ITEMS
from dirbot.spiders.model.quarks.items import ITEMS

class Website(Item):
    # dmoz variables
    dmoz_name = DMOZ_ITEMS.name
    dmoz_description = DMOZ_ITEMS.description
    dmoz_url = DMOZ_ITEMS.url

    # quarks variables
    quarks_title = ITEMS.title
    quarks_link = ITEMS.link
    quarks_description = ITEMS.description
    quarks_pubdate = ITEMS.pubDate

    # dm