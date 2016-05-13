# -*- coding: utf-8 -*-
from dirbot.spiders.const.debug import DEBUG
import logging as LOG

class LOG():
    mode = False

    def __init__(self):
        """
        mode = DEBUG.DEBUG_MODE
        """

    def info(self, msg):
        if self.mode:
            LOG.info(DEBUG.INFO_HEAD + msg)
        else:
            msg

    def debug(self, msg):
        if self.mode:
            LOG.debug(DEBUG.DEBUG_HEAD + msg)
        else:
            msg

    def warn(self, msg):
        if self.mode:
            LOG.warning(DEBUG.WARN_HEAD + msg)
        else:
            msg

    def error(self, msg):
        if self.mode:
            LOG.error(DEBUG.ERROR_HEAD + msg)
        else:
            msg
