# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

from dirbot.spiders.model.dmoz_items import DMOZ_ITEMS
from dirbot.spiders.model.quarks_items import QUARKS_ITEMS

class Website(Item):
    # dmoz variables
    dmoz_name = DMOZ_ITEMS.name
    dmoz_description = DMOZ_ITEMS.description
    dmoz_url = DMOZ_ITEMS.url

    # quarks variables
    quarks_title = QUARKS_ITEMS.title
    quarks_link = QUARKS_ITEMS.link
    quarks_description = QUARKS_ITEMS.description
    quarks_pubdate = QUARKS_ITEMS.pubDate
