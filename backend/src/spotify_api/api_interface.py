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
        self.skiped = pd.DataFrame()
        self.played_emtirely = pd.DataFrame()
        self.token = None
        self.sp = None
        self._update_scope(settings.scope)

    def _update_scope(self, scope: str):
        settings.set_token(scope)
        self.sp = spotipy.Spotify(auth=settings.TOKEN)
        return None

    def get_song_history(self):
        self._update_scope("user-read-recently-played")
        names = []
        songs = []
        song_ids = []
        list_of_all = []
        df = pd.DataFrame(
            list_of_all,
            columns=[
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
                "time_signature",
            ],
        )
        history = self.sp.current_user_recently_played(
            limit=50, after=None, before=None
        )
        history_size = len(history["items"])
        for i in range(history_size):
            song_id = history["items"][i]["track"]["id"]
            song_ids.append(song_id)
            names.append(history["items"][i]["track"]["album"]["artists"][0]["name"])
            songs.append(history["items"][i]["track"]["name"])
            list_of_all.append(self.get_features(song_id))
        df["names"] = names
        df["song"] = songs
        df.drop(
            [
                "type",
                "uri",
                "id",
                "track_href",
                "analysis_url",
                "duration_ms",
                "time_signature",
            ],
            axis=1,
        )
        return df

    def get_current_song(self):
        self._update_scope(scope="user-read-currently-playing")
        current_song = self.sp.currently_playing()
        id_ = current_song["item"]["id"]
        return self.get_features(id_)

    def get_next_song(self) -> pd.Series:
        return None

    def get_playlist_id(self):
        self._update_scope(scope="user-read-currently-playing")
        current_song = self.sp.currently_playing()
        return current_song["context"]["uri"].split(":")[-1]

    def get_features(self, track_id) -> pd.Series:
        features_results = self.sp.audio_features([track_id]) 
        save_path = Path(settings.DATA_PATH, "tmp", "song_features")
        save_path.mkdir(parents=True, exist_ok=True)
        with open(Path(settings.DATA_PATH, "tmp", "song_features", f"{track_id}.json"), "w") as writer:
            json.dump(
                features_results, writer
            )
        features_data = json.load(open(Path(settings.DATA_PATH, "tmp",
                                  "song_features", f"{track_id}.json"), "r"))
        # Convert features dictionary to a list
        return pd.Series(features_data[0])
