from rcon import ConnectionHandler
from rcon import exceptions
from socket import error
import servercfg
import onchatcommands

ip = "YOUR.IP.ADD.RESS"
pw = "YOUR_PASS"
port = 12345


if __name__ == "__main__":
    while True:
        try:
            server = servercfg.Server(ip, port, pw)
            e_server = ConnectionHandler(ip, port, "BF4")\
           .connect()\
           .login(pw)\
           .enable_events() 
        except exceptions.ServerTimeout as e:
            print("Unable to connect")
        except exceptions.InvalidPassword as e:
            print("Wrong password")
        except error as e:
            print("Invalid server address or port number.")
            print("Set the correct values at ip, pw and port variables on the lines 7-9 in main.py.")
        else:
            print("Successfully connected!")
            while True:
                try:
                    event = e_server.process_event()
                except (exceptions.ServerTimeout, exceptions.NoDataReceived) as e:
                    print("Server timeout or no data recevied in event loop.")
                    e_server.reconnect().login(pw).enable_events()
                    print("Reconnected!")
                else:
                    #print(event)
                    if(event[0] == "player.onChat"):
                        onchatcommands.sendcommand(event, server)
        finally:
            exit(0)
