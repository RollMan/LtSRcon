# LtSRcon
A Rcon Tool script for Battlefield 4 Server.

# Introduction
This is Python scripts developed for just LtS, a battlefield 4 clan, that provides functions to manage a battlefield 4 server.  
All features work with Python 2.7.  

# Features
1. Chatted "!rs", the server will be restart the round.
2. Chatted "!chgmap <map> <mode>", the server will change the maps.
3. Chatted "!maplist", the server will show a list of map names.
4. Chatted "!modelist", the server will show a list of mode names.

# Installation
You need to install [frostbite-rcon-utils](https://github.com/EdvinErikson/frostbite-rcon-utils).  
After it, `python main.py` and all features will be available.  

You can use [forever](https://github.com/foreverjs/forever) to make this a daemon.  
`forever start -c python main.py`
