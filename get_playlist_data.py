# Get a playlist from spotify and save data into a file (in .csv)
# Rangsiman

import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy as sp
import json
import csv
import nltk
nltk.downloader.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

from lyricsgenius import Genius

from my_token import *

# Token for connecting to Spotify's API
os.environ["SPOTIPY_CLIENT_ID"] = SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = SPOTIPY_CLIENT_SECRET
# Token for getting lyrics from Genius website - Rangsiman
token=GENIUS_TOKEN

def get_features(track_id):
    features_results = sp.audio_features([track_id])
    json_features = json.dumps(features_results)
    features_data = json.loads(json_features)

    # Convert features dictionary to a list
    features_list = list(features_data[0].values())

    return features_list

client_credentials_manager = SpotifyClientCredentials()
sp = sp.Spotify(client_credentials_manager=client_credentials_manager)
sentiment_analyzer = SIA()

# IDs of monthly playlists from November 2016 to November 2017
playlist_ids = [
    "3B4pbKqnUer2d7DII1QC8Q",
]

# Audio features
feature_names = [
  "danceability",
  "energy",
  "key",
  "loudness",
  "mode",
  "speechiness",
  "acousticness",
  "instrumentalness",
  "liveness",
  "valence",
  "tempo",
  "type",
  "id",
  "uri",
  "track_href",
  "analysis_url",
  "duration_ms",
  "time_signature"
]

username = 'nutty_chem'

### Write data to CSV file
data_file = open('data.csv','w')
writer = csv.writer(data_file)

# Write header
writer.writerow(['track_id', 'playlist_id', 'date_added', 'track_name', 'first_artist'] + feature_names + ['lyrics', 'neg', 'neu', 'pos', 'compound'])

def get_lyrics(song_name, artist_name):
    genius = Genius(token, timeout=100)
    genius.verbose = False
    genius.remove_section_headers = True
    song = genius.search_song(song_name, artist_name)
    try:
        return song.lyrics.replace('\n'," ")
    except:
        return None

for playlist_id in playlist_ids:
    print('Querying playlist: ' + str(playlist_id))

    repeat_query = True
    offset_n = 0
    for i in range(2):
        # Query Spotify API
        if i > 0:
            print('Repeating query')
            offset_n += 100
        results = sp.user_playlist_tracks(username, playlist_id, offset=offset_n)
        json_results = json.dumps(results)
        data = json.loads(json_results)

        # Write rows
        for track in data['items']:
            track_id = track['track']['id']
            date_added = track['added_at']
            track_name = track['track']['name']
            first_artist = track['track']['artists'][0]['name']

            # Track features
            features = get_features(track_id)

            # Try to get lyrics, if available
            lyrics = get_lyrics(track_name, first_artist)

            # Sentiment Analysis
            neg = None
            neu = None
            pos = None
            compound = None
            if lyrics:
                snt = sentiment_analyzer.polarity_scores(lyrics)
                neg = snt['neg']
                neu = snt['neu']
                pos = snt['pos']
                compound = snt['compound']

            writer.writerow([track_id, playlist_id, date_added, track_name, first_artist] + features + [lyrics] + [neg, neu, pos, compound])

        # Special case: API limit is 100 tracks, so we need a second request
        # for playlists that have over 100 tracks
        if data['total'] < 100:
            break

    print('Done querying')

data_file.close()
