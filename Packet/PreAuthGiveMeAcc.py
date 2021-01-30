# -*- coding: utf-8 -*-

from Packet.Writer import Writer


class LoginInit(Writer):

    def __init__(self):
        self.Id = 10101

    def process(self):
        self.putInt(0)
        self.putInt(0)
        self.putString("")
        self.writeInt(26)
        self.writeInt(0)
        self.writeInt(165)
        self.putString('1660a966daa31a498bee59a78670c89ef4364b05')
        self.writeInt(0)
        self.putString('lol')
        
