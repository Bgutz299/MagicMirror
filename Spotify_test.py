import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ae84dd0be57a443ebf92476bc190490a",
                                               client_secret="9c6431a32a9c4bf79dd590b912709e8c",
                                               redirect_uri="http://localhost:8888",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
