# -*- coding: utf-8 -*-

from Packet.Writer import Writer


class SetName(Writer):

    def __init__(self, name):
        self.Id = 10212
        self.name = name
    def process(self):
        self.putString(self.name)

