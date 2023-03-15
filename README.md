# spotify-liked-songs-to-playlist

This script allows you to copy your Liked Songs on Spotify to an actual playlist.

This solves an issue where Spotify won't play your Liked Songs on devices other than mobile.

Setup:

1. Install spotipy using pip
2. Create a new playlist or choose an existing one within the Spotify webapp
3. Copy its id from the url in your browser (Example: https://open.spotify.com/playlist/[playlist id])
4. Paste the id into the playlist_id variable on line 5 of spot.py
5. Set up a Spotify app at: https://developer.spotify.com/dashboard/
6. Click the Edit Settings button
7. Add 'http://localhost:8888' as a Redirect URI for your app
8. Export your client id - Example: export SPOTIPY_CLIENT_ID=[your id goes here]
9. Export your client secret - Example: export SPOTIPY_CLIENT_SECRET=[your secret goes here]
10. Export your redirect uri - Example: export SPOTIPY_REDIRECT_URI=http://localhost:8888
11. Run spot.py

Enjoy!

