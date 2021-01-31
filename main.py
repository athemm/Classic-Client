#!/usr/bin/python3

import os
import sys
import json
import socket
import progressbar
import random
import string
import threading
import time
from Packet.Packet_Factory import *

# Packet factory:

# class Server.
# SendSetNameMessage()
# SendLoginMessage()
# SendKeepAlive()

# CanIHasAccount(socket)

from Packet.sequences import *

from Packet.Reader import CoCMessageReader
from Packet.Writer import Write
from Packet.PreAuth import PreAuth
from Packet.SetName import SetName
from Packet.KeepAlive import KeepAlive

def choice_thread(server, my_token):
    print("""\n----------------------\n\nWhat would you like to do?
      1 - Add 3v3 win
      2 - Open Mega box
      3 - Open Big box
      4 - Add solo sd win
      5 - Send club message
      6 - Create game room
      7 - 31"""+" çek" * 5 + """
      8 - break server (available in pro version only 1 discord nitro to buy!!!)
      9 - """)
    c = int(input("Your choice: "))

    if c == 1: 
        server.me_want_trophy()
        print("ok")
        server.r() 

        # recieve everything
        # you get home data too i think
        # appearantly you don't

    if c == 2: 
        server.me_want_mega_box()
        print("ok opened mega box")

    if c == 3: 
        pass

    if c == 4: 
        server.me_want_more_trophy()
        print("ok")
        server.r() 

    if c == 5: 
        pass

    if c == 6: 
        pass

    if c == 7: 
        pass

    if c == 8: pass

    if c == 9: 
        pass

    choice_thread(server, my_token) # recurse



def recvall(sock, size):
    data = []
    while size > 0:
        sock.settimeout(5.0)
        s = sock.recv(size)
        sock.settimeout(None)
        if not s:
            raise EOFError
        data.append(s)
        size -= len(s)
    return b''.join(data)

def recv(s):
    header = s.recv(7)
    size = int.from_bytes(header[2:5], 'big')
    data = recvall(s, size)
    return data, header

def client_thread():

    iAmNew = False
    s = socket.socket()
    s.connect(("192.168.0.19",9339))
    if not os.path.isfile("credentials.txt"):
        iAmNew = True
        my_token = initSeq(s)
        open("credentials.txt", "w").write(my_token)
    else:
        my_token = open("credentials.txt", "r").read()

    server = Server(s, 4) # (socket, int length)

    # Login
    if not iAmNew:
        server.SendLoginMessage(my_token)

    time.sleep(0.7)
    poop = s.recv(4096)
    print("Log in done")
    # debug
    #print(poop)

    threading.Thread(target=choice_thread, args=[server, my_token]).start()
    print("Started choice thread\n")
    while True:
        server.SendKeepAlive()


        


        time.sleep(4)
        
client_thread()


#    THE GREAT UNUSED STUFF REMNANT
#     HERE LIES THE UNUSED THINGS


# int(input("Thread count > "))
#count = 5
#logs = Logs("logfile.txt")
#logs.write("oi")
#logs.write("shit")
#logs.write("jk")
#logs.erase("jk")

#server.crash(1000000)

