import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

cid = 'ae84dd0be57a443ebf92476bc190490a'
secret = '9c6431a32a9c4bf79dd590b912709e8c'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

user =sp.user('Exedranoid')

result = sp.current_user_followed_artists(limit=20, after=None)