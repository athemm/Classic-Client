# -*- coding: utf-8 -*-

from Packet.Writer import Writer


class KeepAlive(Writer):

    def __init__(self):
        self.Id = 10108
    def process(self):
        pass
