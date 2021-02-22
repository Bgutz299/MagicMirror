import spotipy
import requests
import os
import sys
import json
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

def spotify_control():
    cid = 'ae84dd0be57a443ebf92476bc190490a'
    secret = '9c6431a32a9c4bf79dd590b912709e8c'
    uri = 'https://Smartmirror.com/auth'
    username = ''
    scope = 'user-read-private user-read-playback-state user-modify-playback-state'

    token = spotipy.util.prompt_for_user_token(username = username, scope=scope, client_id=cid, client_secret=secret, redirect_uri='https://Smartmirror.com/auth', cache_path=None)
    sp = spotipy.Spotify(auth = token)
    # User information
    user = sp.current_user()
    displayName = user['display_name']
    follower = user['followers']['total']
    #print(user)
    print(displayName)
    print(follower)
