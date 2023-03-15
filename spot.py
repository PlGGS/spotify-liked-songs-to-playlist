import spotipy
from spotipy.oauth2 import SpotifyOAuth

# READ THE README AND THEN SET THIS BEFORE RUNNING
playlist_id = ''

scope = "user-library-read playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

print('getting tracks. This will take a bit...')
# https://stackoverflow.com/questions/39086287/spotipy-how-to-read-more-than-100-tracks-from-a-playlist
def get_liked_songs():
    results = sp.current_user_saved_tracks()
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
        
    # We reverse the tracks, because Liked Songs on Spotify are added top to bottom
    return reversed(tracks)

for idx, item in enumerate(get_liked_songs()):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
    sp.playlist_add_items(playlist_id, [track['uri']])  
