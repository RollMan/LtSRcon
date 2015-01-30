from rcon import ConnectionHandler
from rcon import exceptions

ip = "YOUR.IP.ADD.RESS."
pass = "YOUR_PASSWORD"
port = YOUR_PORT

def restart():
  return address.connect().login(pass).command("mapList.restartRound")

if __name__ == "__main__":
  try:
    address = ConnectionHandler(ip, port, "bf4")
    server = address\
         .connect()\
         .login(pass)\
         .enable_events() 

  except exceptions.ServerTimeout as e:
    print("Unable to connect")
  
  except exceptions.InvalidPassword as e:
    print("Wrong password")
  
  else:
    print("Successfully connected!")
  while True:
    try:
      event = server.process_event()
    except (exceptions.ServerTimeout, exceptions.NoDataReceived) as e:
      print("Server timeout or no data recevied in event loop.")
      server.reconnect().login(pass).enable_events()
      print("Reconnected!")
    else:
      #print(event)
      if(event[0] == "player.onChat" and event[2] == "!rs"):
        print restart()
  
