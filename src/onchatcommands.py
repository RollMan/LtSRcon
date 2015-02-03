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
    option = []
    order  = event[2].split()[0]
    if " " in event[2]:
        option = event[2].split()
        del option[0]
    if order[0] != '!':
        return ["Not command"]
    elif order == "!rs":
        result.append(server.sndcmd("mapList.restartRound"))
    
    elif order == "!help":
        result.append(server.sndcmd("admin.say", ["!rs, !chgmap <map> <mode>, !mapList, !modeList", "all"]))
    
    elif order == "!chgmap":
        if len(option) != 2:
            result.append(server.sndcmd("admin.say", ["Usage: !chgmap <map> <mode>", "all"]))
        elif option[0] not in mapdic or option[1] not in modedic:
            result.append(server.sndcmd("admin.say", ["No such a map or mode.", "all"]))
        else:
            result.append(server.sndcmd("mapList.clear"))
            result.append(server.sndcmd("mapList.add", [mapdic[option[0]], modedic[option[1]], 1]))
            result.append(server.sndcmd("mapList.runNextRound"))
        
    elif(order == "!maplist"):
        try:
            line = ""
            for key in mapdic:
                if len(line) > 100:
                    result.append(server.sndcmd("admin.say", [line, "all"]))
                    line = ""
                else:
                    line += key + ","
            result.append(server.sndcmd("admin.say", [line, "all"]))
        
        except Exception as e:
            message = "ERROR: type:" + type(e) + " args:" + str(e.args)
            result.append(message)

    elif(order == "!modelist"):
        try:
            line = ""
            for key in modedic:
                if len(line) > 100:
                    result.append(server.sndcmd("admin.say", [line, "all"]))
                    line = ""
                else:
                    line += key + ","
            result.append(server.sndcmd("admin.say", [line, "all"]))
        
        except Exception as e:
            message = "ERROE: type:" + type(e) + "args:" + str(e.args)
            result.append(message)
    else:
        result.append(server.sndcmd("admin.say", ["No such a command", "all"]))
        return ["No such a command"]
    
    return result
