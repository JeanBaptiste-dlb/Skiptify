import spotipy
import spotipy.util as util
from src.config import settings


def sing():
    if settings.token:
        # Create a Spotify() instance with our token
        sp = spotipy.Spotify(auth=settings.token)

        # method currently playing return an actual song on Spotify
        current_song = sp.currently_playing()

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


# # Way 1
# song = genius.search_song("To You", artist.name)
# song = artist.song("To You")
# print(song.lyrics)

if __name__ == "__main__":
    # while True:
    # raw_song_name , wait = sing()
    song_name, artist_name = sing()