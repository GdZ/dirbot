# -*- coding: utf-8 -*-
from dirbot.spiders.model.mybb_filter import MYBB_FILTER
import logging as LOG

class MYBB_ACTION():
    """
    get filter,
    """
    selector = []
    items = []
    def __init__(self, selector):
        """
        init etw.
        """
        self.selector = selector

    def run(self):
        mybb_filter = MYBB_FILTER()
        local_filter = MYBB_FILTER(self.selector)
        local_filter.run()
        self.items = local_filter.arrays
        LOG.debug("items: " + self.items.__str__())