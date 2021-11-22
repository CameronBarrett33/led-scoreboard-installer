#! /bin/bash

if (systemctl -q is-active mlb-led-scoreboard.service)
then
    sudo systemctl disable mlb-led-scoreboard.service
    sudo systemctl enable nfl-led-scoreboard.service
    sudo service nfl-led-scoreboard start

elif (systemctl -q is-active nfl-led-scoreboard.service)
 then
    sudo systemctl disable nfl-led-scoreboard.service
    sudo systemctl enable nhl-led-scoreboard.service
    sudo service nhl-led-scoreboard start

elif (systemctl -q is-active nhl-led-scoreboard.service)
  then
    sudo systemctl disable nhl-led-scoreboard.service
    sudo systemctl enable mlb-led-scoreboard.service
    sudo service mlb-led-scoreboard start
 else
    sudo systemctl enable mlb-led-scoreboard.service
    sudo service mlb-led-scoreboard start
    
fi
