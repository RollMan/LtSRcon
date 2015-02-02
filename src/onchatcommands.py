# -*- coding: utf-8 -*-

mapdic = {"Locker"  :"MP_Prison",
          "Zavod"   :"MP_Abandoned",
          "Dam"     :"MP_Damage",
          "Flood"   :"MP_Flooded",
          "Railway" :"MP_Journey",
          "Paracel" :"MP_Naval",
          "Hainan"  :"MP_Resort",
          "Shanghai":"MP_Siege",
          "Rogue"   :"MP_TheDish",
          "Dawn"    :"MP_Tremors",
          "Silk"    :"XP1_001",
          "Altai"   :"XP1_002",
          "GPeaks"  :"XP1_003",
          "DPass"   :"XP1_004",
          "Caspian" :"XP0_Caspia",
          "FStorm"  :"XP0_FireStor",
          "Metro"   :"XP0_Metro",
          "Oman"    :"XP0_Oman",
          "LIsland" :"XP2_001",
          "Nansha"  :"XP2_002",
          "WBreaker":"XP2_003",
          "OMortar" :"XP2_004",
          "PMarket" :"XP3_MarketPl",
          "Propag"  :"XP3_Prpganda",
          "LGarden" :"XP3_UrbanGdn",
          "SDragon" :"XP3_WtrFront",
          "Whiteout":"XP4_Arctic",
          "Hammer"  :"XP4_SubBase",
          "Hanger"  :"XP4_Titan",
          "Giant"   :"XP4_WalkerFactory"
         }

modedic = {"cqL":"ConquestLarge0",
           "cqS":"ConquestSmall0",
           "dmn":"Domination0",
           "tdm":"TeamDeathMatch0",
           "rsh":"RushLarge0",
           "obl":"Obliteration",
           "dfs":"Elimination0",
           "std":"SquadDeathMatch0",
           "air":"AirSuperiority0",
           "cap":"CaptureTheFlag0",
           "caS":"CarrierAssaultSmall0",
           "caL":"CarrierAssaultLarge0",
           "lnk":"Chainlink0"
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
    elif(order.split()[0] == "!maplist":
        maps = []
        line = ""
        for key in mapdic.iterkeys():
            maps.append(key)
        line.join(maps)
        result.append(server.sndcmd("admin.say", [line, all]))
    elif(order.split()[0] == "!modelist":
        modes = []
        line = ""
        for key in modedic.iterkeys():
            modes.append(key)
        line.join(modes)
        result.append(server.sndcmd("admin.say", [line, all]))
    else:
        return "Command Error"
  
    return result
