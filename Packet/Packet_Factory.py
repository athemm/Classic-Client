from Packet.Reader import CoCMessageReader
from Packet.Writer import Write
from Packet.PreAuth import PreAuth
from Packet.PreAuthGiveMeAcc import LoginInit
from Packet.SetName import SetName
from Packet.KeepAlive import KeepAlive
import random
import string 
from Packet.Reader import CoCMessageReader

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

class Server:

        def __init__(self, client, name_len):
                self.client = client
                self.name_len = name_len

        def me_want_trophy(self):
                self.client.send(open("trophies.bin", "rb").read())

        def get_random_name(self):
                return ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.name_len))

        def SendSetNameMessage(self):
                name = self.get_random_name()
                self.client.send(Write(SetName(name)))

        def SendKeepAlive(self):
                self.client.send(Write(KeepAlive()))

        def SendLoginMessage(self, my_token):
                self.client.send(Write(PreAuth(my_token)))

def CanIHasAccount(s):
        s.send(Write(LoginInit()))
        raw_login, _id = recv(s)
        print("Getting message",int.from_bytes(_id[0:2], "big"))
        data = CoCMessageReader(raw_login)

        print("Parsing message...")
        hid = data.read_int()
        print("High id:",hid)

        data.read_int() # trash
        data.read_int() # id agian
        data.read_int() # eeeeee

        _token = data.read_string()
        print("Token:", _token)

        name = "shit_even"

        if name == "":
            print("enter a name") #retard")
            CanIHasAccount(s)

        s.send(Write(SetName(name)))
        # print("try recv")
        mylastmessage, savedaworld = recv(s)
        # print("poo")
        return _token, name, mylastmessage
        
        
                
                
