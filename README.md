# spotify-liked-songs-to-playlist

This script allows you to copy your Liked Songs on Spotify to an actual playlist.

This solves an issue where Spotify won't play your Liked Songs on devices other than mobile.

Setup:

1. Install spotipy using pip
2. Set up a Spotify app at: https://developer.spotify.com/dashboard/
3. Click the Edit Settings button
4. Add 'http://localhost:8888' as a Redirect URI for your app
5. Export your client id - Example: export SPOTIPY_CLIENT_ID=[your id here]
6. Export your client secret - Example: export SPOTIPY_CLIENT_SECRET=[your secret here]
7. Export your redirect uri - Example: export SPOTIPY_REDIRECT_URI=http://localhost:8888
8. Create a new playlist or choose an existing one within the Spotify webapp
9. Copy its id from the url in your browser - Example: https://open.spotify.com/playlist/[playlist id]
10. Run spot.py with your playlist id as a command line argument - Example: python3 spot.py [your id here]

Enjoy!
