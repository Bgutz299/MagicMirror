import spotipy
import requests
import os
import sys
import json
import webbrowser
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

cid = 'ae84dd0be57a443ebf92476bc190490a'
secret = '9c6431a32a9c4bf79dd590b912709e8c'
uri = 'https://Smartmirror.com/auth'
username = ''
scope = 'user-read-private user-read-playback-state user-modify-playback-state'
##
###r = requests.get('https://accounts.spotify.com/authorize')
###OAUTH_AUTHORIZE_URL= 'https://accounts.spotify.com/authorize'
###OAUTH_TOKEN_URL = "https://accounts.spotify.com/api/token"
##
token = spotipy.util.prompt_for_user_token(username = username, scope=scope, client_id=cid, client_secret=secret, redirect_uri='https://Smartmirror.com/auth', cache_path=None)
sp = spotipy.Spotify(auth = token)

# User information
user = sp.current_user()
displayName = user['display_name']
follower = user['followers']['total']
#print(user)
print(displayName)
print(follower)

devices = sp.devices()
print(json.dumps(devices, sort_keys=True, indent=4))
for i in range(len(devices['devices'])):
    if(devices['devices'][i]['name'] == "Mira"):
        deviceID = devices['devices'][i]['id']
print(deviceID)
#print(len(devices['devices']))

# Get track information
track = sp.current_user_playing_track()
print(track)
print(json.dumps(track, sort_keys=True, indent=4))
print()
if(track != None):
    artist = track['item']['artists'][0]['name']
    track = track['item']['name']
    if artist !="":
        print("Currently playing " + artist + " - " + track)
 
# User information
user = sp.current_user()
displayName = user['display_name']
follower = user['followers']['total']



while True:

    print()
    print(">>> Welcome to Spotify " + displayName + " :)")
    print(">>> You have " + str(follower) + " followers.")
    print()
    print("0 - Search for an artist")
    print("1 - exit")
    print()
    choice = input("Enter your choice: ")


    # Search for artist
    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name?:")
        print()
        # Get search results
        searchResults = sp.search(searchQuery,1,0,"artist")

        # Print artist details
        artist = searchResults['artists']['items'][0]
        print(artist['name'])
        print(str(artist['followers']['total']) + " followers")
        print(artist['genres'][0])
        print()
        #webbrowser.open(artist['images'][0]['url'])
        artistID = artist['id']

        # Album details
        trackURIs = []
        trackArt = []
        z = 0


        # Extract data from album
        albumResults = sp.artist_albums(artistID)
        albumResults = albumResults['items']

        for item in albumResults:
            print("ALBUM: " + item['name'])
            albumID = item['id']
            albumArt = item['images'][0]['url']

        # Extract track data
        trackResults = sp.album_tracks(albumID)
        trackResults = trackResults['items']

        for item in trackResults:
            print(str(z) + ": " + item['name'])
            trackURIs.append(item['uri'])
            trackArt.append(albumArt)
            z+=1
        print()

        # See album art
        while True:
            songSelection = input("Enter a song number to see the album art: ")
            if songSelection == "x":
                break
            trackSelectionList = []
            trackSelectionList.append(trackURIs[int(songSelection)])
            sp.start_playback(deviceID, None, trackSelectionList)
            webbrowser.open(trackArt[int(songSelection)])
    # End program
    elif choice == "1":
        break
#spauth = spotipy.SpotifyOAuth(client_id = cid, client_secret = secret, redirect_uri = uri, , scope = scope, open_browser = True)
# spauth.get_authorize_url()
# spauth.get_access_token()

#username ='Exedranoid'

#token = util.prompt_for_user_token(username, scope)
