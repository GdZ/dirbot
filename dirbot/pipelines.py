# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem


class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    words_to_filter = ['politics', 'religion']

    def process_item(self, item, spider):
        for word in self.words_to_filter:
            # if word in unicode(item['description']).lower():
<<<<<<< HEAD
            #     raise DropItem("Contains forbidden word: %s" % word)
            if word in unicode(item['value']).lower():
                raise DropItem("Contains forbidden word: %s" % word)
        else:
            return item
=======
            # if word in unicode(item['value']).lower():
            #     raise DropItem("Contains forbidden word: %s" % word)
            # else:
                return item
>>>>>>> f86b705298f70d7354b7ec1cb48ff8518a920bc0
