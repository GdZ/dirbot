# -*- coding: utf-8 -*-

from scrapy.item import Item, Field

from dirbot.spiders.model.dmoz_items import DMOZ_ITEMS

class Website(Item):

    name = DMOZ_ITEMS.name
    description = DMOZ_ITEMS.description
    url = DMOZ_ITEMS.url
