# -*- coding: utf-8 -*-

mapdic = {"Locker":"MP_Prison", "Zavod":"MP_Abandoned"}
modedic = {"cqL":"ConquestLarge0",
           "cqS":"ConquestSmall0",
           "dmn":"Domination0",
           "tdm":"TeamDeathMatch0",
           "rsh":"RushLarge0",
           "obl":"Obliteration"
          }

def sendcommand(event, server):
    result = []
    order = event[2]
    if order[0] != '!':
        return "Not command"
    elif order == "!rs":
        result.append(server.sndcmd("mapList.restartRound"))
    elif order.split()[0] == "!chgmap":
        result.append(server.sndcmd("mapList.clear"))
        result.append(server.sndcmd("mapList.add", [mapdic[order.split()[1]], modedic[order.split()[2]], 1]))
        result.append(server.sndcmd("mapList.runNextRound"))
    
  
    else:
        return "Command Error"
  
    return result