import spotipy
# import spotipy.util as util
from lyricsgenius import Genius

# Import token for getting song's info from Spotify,
# and also token for Genius website
from my_token import *


scope = 'user-read-currently-playing'

# To connect succesfully you need to provide your own Spotify Credentials
# You can do this signing up in https://developer.spotify.com/ and creating a new app.
token = spotipy.util.prompt_for_user_token(
    USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)


def sing():
    if token:
        # Create a Spotify() instance with our token
        sp = spotipy.Spotify(auth=token)

        # method currently playing return an actual song on Spotify
        current_song = sp.currently_playing()
        print(current_song)

        # Extract artist from json response
        artist = current_song['item']['artists'][0]['name']
        # Extract song name from json response
        song_name = current_song['item']['name']

        # create a valid url for web scrapping using song name and artist
        song_url = '{}-{}-lyrics'.format(str(artist).strip().replace(' ', '-'),
                                         str(song_name).strip().replace(' ', '-'))

        print('\nSong: {}\nArtist: {}'.format(song_name, artist))

    else:
        print("Can't get token for")

    # return (song_url , (current_song['item']['duration_ms'] - current_song['progress_ms']) / 1000)
    return song_name, artist


def get_lyrics(song_name, artist_name):
    genius = Genius(GENIUS_TOKEN)
    song = genius.search_song(song_name, artist_name)
    return song.lyrics

# # Way 1
# song = genius.search_song("To You", artist.name)
# song = artist.song("To You")
# print(song.lyrics)


if __name__ == "__main__":
    # while True:
    # raw_song_name , wait = sing()
    song_name, artist_name = sing()
    lyrics = get_lyrics(song_name, artist_name)
    print(lyrics.strip())
