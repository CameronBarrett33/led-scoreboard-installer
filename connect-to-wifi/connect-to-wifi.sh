#! /bin/bash

# clear all contents of wpa_supplicant.config
sudo sh -c 'cat /led-scoreboard-installer/connect-to-wifi/clear-wpa_supplicant.config > /etc/wpa_supplicant/wpa_supplicant.config'

sudo sh -c 'wpa_passphrase ${1} ${2} >> /etc/wpa_supplicant/wpa_supplicant.conf'