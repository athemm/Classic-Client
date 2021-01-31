# -*- coding: utf-8 -*-

from Packet.Writer import Writer


class PreAuth(Writer):

    def __init__(self, token):
        self.Id = 10101
        self.token = token

    def process(self):
        self.putInt(0)
        self.putInt(0)
        self.putString(self.token)
        self.writeInt(26)
        self.writeInt(0)
        self.writeInt(165)
        self.putString('1660a966daa31a498bee59a78670c89ef4364b05')
        self.writeInt(0)
        self.putString('nyb')
        self.putString('nyb')
        self.putString('nyb')
        
