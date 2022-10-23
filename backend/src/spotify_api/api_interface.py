import json
import numpy as np
import pandas as pd
import spotipy
from backend.src.config import settings
import spotipy.util as util
from pathlib import Path
from datetime import datetime


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
        try:
            self._update_scope(scope="user-read-currently-playing")
            current_song = self.sp.currently_playing()
            id_ = current_song["item"]["id"]
            return self.get_features(id_)
        except TypeError:
            print("No song is currently playing.")
            return None
        

    def save_song_features(self, features=pd.Series, skip_state="UNKNOWN", skip_probability=0):
        """
        Skip state can be "UNKNOWN", "SKIPPED", "NOT SKIPPED".
        """
        save_path = Path(settings.DATA_PATH, "tmp", "song_features")
        save_path.mkdir(parents=True, exist_ok=True)
        with open(
            Path(settings.DATA_PATH, "tmp", "song_features", f"{features['id']}.json"), "w"
        ) as writer:
            features["skip_state"] = skip_state
            features["date_saved"] = str(datetime.now())
            features["skip_probability"]= skip_probability
            json.dump(dict(features), writer)

    def load_song_features(self, song_id) -> pd.Series:
        with open(
            Path(settings.DATA_PATH, "tmp", "song_features", f"{song_id}.json"), "r"
        ) as reader:
            features = json.load(reader)
        return pd.Series(features)

    def get_next_song(self, sp):
        """Get the next song in the currently playing playlist

        Args:
            sp (_type_): Spotipy authentication

        Returns:
            track_id of the next song
            track_name of the next song
        """
        self._update_scope("user-read-currently-playing")
        # Get all tracks of the given playlist
        # playlist_id = "3B4pbKqnUer2d7DII1QC8Q"
        offset_n = 0
        results = self.sp.user_playlist_tracks(self.sp.me()['id'], self.get_playlist_id(), offset=offset_n)
        json_results = json.dumps(results)
        data = json.loads(json_results)
        # Get id of all tracks
        all_track_id = []
        all_track_name = []
        for track in data['items']:
            track_id = track['track']['id']
            date_added = track['added_at']
            track_name = track['track']['name']
            all_track_id.append(track_id)
            all_track_name.append(track_name)

        # get currently playing song
        current_song = sp.currently_playing()
        current_song_id = current_song['item']['id']
        idx_next_song = all_track_id.index(current_song_id) + 1
        return all_track_id[idx_next_song]

    def get_playlist_id(self):
        self._update_scope(scope="user-read-currently-playing")
        current_song = self.sp.currently_playing()
        return current_song["context"]["uri"].split(":")[-1]

    def get_features(self, track_id) -> pd.Series:
        features_results = self.sp.audio_features([track_id])
        return pd.Series(features_results[0])

    def get_metadata_current(self):
        name = self.sp.currently_playing()["item"]["name"]
        artist_name = self.sp.currently_playing()['item']['album']['artists'][0]['name']
        album_image_url = self.sp.currently_playing()['item']['album']['images'][0]['url']
        metadata = [name, artist_name, album_image_url]
        test = pd.DataFrame(metadata, columns=["current_song"], index=["name", "album", "url"])
        return test


