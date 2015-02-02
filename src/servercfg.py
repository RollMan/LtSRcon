from rcon import ConnectionHandler
from rcon import exceptions

class Server:
    ip = ""
    port = 0
    pw = ""
    def __init__(self, ip, port, pw):
        self.ip = ip
        self.port = port
        self.pw = pw

    def sndcmd(self, commandreq, arg=[]):
        ConnectionHandler(self.ip, self.port, "bf4").connect().login(self.pw).command(commandreq, arg)
