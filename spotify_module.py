import spotipy
import requests
import os
import sys
import json
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

from guizero import App,Text,ButtonGroup,PushButton,TextBox,Drawing,Box,Window

global scope
global sp
global deviceID
global volume

scope = 'user-read-private user-read-playback-state user-modify-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
devices = sp.devices()
for i in range(len(devices['devices'])):
        if(devices['devices'][i]['name'] == "Mira"):
            deviceID = devices['devices'][i]['id']
def play():
    global sp
##    # User information
##    user = sp.current_user()
##    displayName = user['display_name']

    #devices = sp.devices()
    #print(json.dumps(devices, sort_keys=True, indent=4))
    sp.start_playback(device_id=deviceID)
    #print(displayName)
    #print(auth.get_cached_token())

def pause():

    #print(json.dumps(devices, sort_keys=True, indent=4))
    sp.pause_playback(device_id=deviceID)

def fetch_volume():
    for i in range(len(devices['devices'])):
        if(devices['devices'][i]['id'] == deviceID):
            volume = devices['devices'][i]['volume_percent']
    return volume

volume = fetch_volume()

def volume_up():
    global volume
    if(volume + 5 <= 100):
        volume = volume + 5
        sp.volume(volume, device_id=deviceID)
    return volume

def volume_down():
    global volume
    if(volume - 5 >= 0):
        volume = volume - 5
        sp.volume(volume, device_id=deviceID)
    return volume

def close(app):
    play()
    app.tk.destroy


    

