import pandas as pd
import spotipy
from backend.src.config import settings
import spotipy
import spotipy.util as util
import json
import numpy as np
from pathlib import Path

class SPOTIFY_API_INTERFACE:
    def __init__(self) -> None:
        self.scope = settings.scope
        self.token = spotipy.util.prompt_for_user_token(
            settings.USERNAME, settings.scope, client_id=settings.SPOTIPY_CLIENT_ID, client_secret=settings.SPOTIPY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIPY_REDIRECT_URI)
        self.sp = spotipy.Spotify(auth=self.token)
        self.skiped=pd.DataFrame()
        self.played_emtirely=pd.DataFrame()

    def _update_scope(self, scope:str):
        self.token = spotipy.util.prompt_for_user_token(
            settings.USERNAME, settings.scope, client_id=settings.SPOTIPY_CLIENT_ID, client_secret=settings.SPOTIPY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIPY_REDIRECT_URI)
        self.sp=spotipy.Spotify(auth=self.token)
        return None
    

    def get_song_history(self):
        self._update_scope()
        names = []
        songs = []
        song_ids = []
        list_of_all = []
        df = pd.DataFrame(list_of_all, columns=["danceability",
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
                                        "time_signature"])
        history = self.sp.current_user_recently_played(limit=50, after=None, before=None)
        for i in range(50):
            song_id = history['items'][i]['track']['id']
            song_ids.append(song_id)
        for i in range(50):
            names.append(history['items'][i]['track']['album']['artists'][0]['name'])
            songs.append(history['items'][i]['track']['name'])
        for i in range(50):
            list_of_all.appends(self.get_features(song_ids[i]))
        df['names'] = names
        df['song'] = songs
        df.drop(['type','uri','id',  "track_href","analysis_url","duration_ms", "time_signature"], axis=1)
        return df

    def get_current_song(self):
        self._update_scope(scope = 'user-read-currently-playing')
        current_song = self.sp.currently_playing()
        id_=current_song['item']['id']
        return self.get_features(id_)

    def get_next_song(self) -> pd.Series:
        return None

            

    def get_features(self, track_id) -> pd.Series:
        features_results = self.sp.audio_features([track_id])
        json_features = json.dumps(features_results, Path(settings.DATA_PATH, "tmp", "song_feature.json"))
        features_data = json.loads(json_features)
        # Convert features dictionary to a list
        features_list = list(features_data[0].values())
        return pd.Series(features_list)


