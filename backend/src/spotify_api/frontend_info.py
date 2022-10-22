import spotipy
# -----------------
# Token for getting song's info from Spotify
USERNAME = "nellen.noemi"
SPOTIPY_CLIENT_ID = "e4470f9d03054bdfae83ea6a54c68b58"
SPOTIPY_CLIENT_SECRET = "abf880a5bf454d7e94eb8905bd02c982"
SPOTIPY_REDIRECT_URI = "https://example.com/callback"

# Token for getting lyrics from Genius website - Rangsiman
token = ""
# -----------------

scope = 'user-read-currently-playing'

# To connect succesfully you need to provide your own Spotify Credentials
# You can do this signing up in https://developer.spotify.com/ and creating a new app.
token = spotipy.util.prompt_for_user_token(
    USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)
current_song = sp.currently_playing()
