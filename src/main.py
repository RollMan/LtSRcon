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
            servercfg.logging("Unable to connect")
            exit(0)
        except exceptions.InvalidPassword as e:
            servercfg.logging("Wrong password")
            print("Wrong password")
            exit(0)
        except error as e:
            servercfg.logging("Invalid server address or port number.")
            servercfg.logging("Set the correct values at ip, pw and port variables on the lines 7-9 in main.py.")
            print("Invalid server address or port number.")
            print("Set the correct values at ip, pw and port variables on the lines 7-9 in main.py")
            exit(0)
        else:
            servercfg.logging("Successfully connected!")
            print("Successfully connected!")
            while True:
                try:
                    event = e_server.process_event()
                except (exceptions.ServerTimeout, exceptions.NoDataReceived) as e:
                    servercfg.logging("Server timeout or no data recevied in event loop.")
                    print("Server timeout or no data received in event loop.")
                    e_server.reconnect().login(pw).enable_events()
                    servercfg.logging("Reconnected!")
                    print("Reconnected!")
                else:
                    #print(event)
                    if(event[0] == "player.onChat"):
                        logs = onchatcommands.sendcommand(event, server)
                        for i in range(len(logs)):
                            if logs[i] is None:
                                logs[i] = "None"
                        servercfg.logging("\n                        ".join(logs))
