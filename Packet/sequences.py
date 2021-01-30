from Packet.Packet_Factory import *
from Packet.Reader import CoCMessageReader
from Packet.Writer import Write
from Packet.PreAuth import PreAuth
from Packet.SetName import SetName
from Packet.KeepAlive import KeepAlive

# i just realized this file is totally useless...
# may as well just keep it
# idk it might break if i remove it so
# i dont think i care

def initSeq(s):
    token, name, name_recv = CanIHasAccount(s)
   # debug
    #print(name)
    #print(token)
    #print(name_recv)

    return token


