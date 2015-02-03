from rcon import ConnectionHandler
import datetime

def logging(content):
    f = open("log.txt", "a+")
    d = datetime.datetime.today()
    f.write("{:0>4}/{:0>2}/{:0>2} | {:0>2}:{:0>2}:{:0>2} : "
            .format(d.year, d.month, d.day, d.hour, d.minute, d.second)
            + content + "\n")
    f.close()

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
