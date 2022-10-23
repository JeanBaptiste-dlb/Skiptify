import spotipy
# import spotipy.util as util
from lyricsgenius import Genius
import json
import pandas as pd
import numpy as np

from sklearn.metrics import pairwise_distances

# Import token for getting song's info from Spotify,
# and also token for Genius website
from my_token import *    

scope = 'user-read-currently-playing'
# scope = 'user-modify-playback-state'
# scope = 'user-read-recently-played'

# To connect succesfully you need to provide your own Spotify Credentials
# You can do this signing up in https://developer.spotify.com/ and creating a new app.
token = spotipy.util.prompt_for_user_token(
    USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)

sp = spotipy.Spotify(auth=token)

def get_features_to_list(track_id):
    features_results = sp.audio_features([track_id])
    json_features = json.dumps(features_results)
    features_data = json.loads(json_features)

    # Convert features dictionary to a list
    features_list = list(features_data[0].values())
    return features_list

def calc_dist(feature1, feature2):
    dss = np.vstack((feature1, feature2))
    distance_matrix = pairwise_distances(dss)
    return distance_matrix[0][1]

def is_song_skipped(track_id):
    """Check if the given is skipped based on distance

    Args:
        track_id (str): id of the song to check if it should be skipped
    
    Return:
        True: skip
        False: skip
    """
    # self.sp._update_scope("user-read-currently-playing")
    # get features of the skipped songs
    df_skipped = pd.read_csv('../../../data/player_data/skipped.csv', usecols=[i for i in range(11)])
    normalized_d_skipped = (df_skipped - df_skipped.mean()) / (df_skipped.max() - df_skipped.min())

    # get features of the non-skipped songs
    df_nonskipped = pd.read_csv('../../../data/player_data/non_skipped.csv', usecols=[i for i in range(11)])
    normalized_d_nonskipped = (df_nonskipped - df_nonskipped.mean()) / (df_nonskipped.max() - df_nonskipped.min())

    # get features of the song to check the similarity distance
    feature1 = get_features_to_list(track_id)
    feature1 = feature1[:11]

    # calc distance to the skipped
    distances_skipped = []
    for i in range(len(normalized_d_skipped)):
        feature2 = normalized_d_skipped.iloc[i,:]
        dist_tmp = calc_dist(feature1, feature2)
        distances_skipped.append(dist_tmp)

    # calc distance to the skipped
    distances_nonskipped = []
    for i in range(len(normalized_d_nonskipped)):
        feature3 = normalized_d_nonskipped.iloc[i,:]
        dist_tmp = calc_dist(feature1, feature3)
        distances_nonskipped.append(dist_tmp)

    # compare distances
    dist_skipped = np.array(distances_skipped).mean()
    dist_nonskipped = np.array(distances_skipped).mean()
    if dist_skipped > dist_nonskipped:
        return False
    else:
        return True

# Test with a random track
id = '3ZOD3aghbxBkgKsLu2jOEK'
print(is_song_skipped(id))
