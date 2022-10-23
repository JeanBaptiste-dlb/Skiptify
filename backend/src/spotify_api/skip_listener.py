import pandas as pd
import spotipy
from backend.src.config import settings
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE
import spotipy.util as util
import json
import numpy as np
from pathlib import Path
import time
from datetime import datetime
from backend.src.spotify_api.spotify_actioner import SpotifyActioner


class SKIP_LISTENER:
    def __init__(self):
        self.scope = settings.scope
        self.skiped = pd.DataFrame()
        self.played_emtirely = pd.DataFrame()
        self.interface = SPOTIFY_API_INTERFACE()
        self.current_song = None
        self.previous_song = None
        self.end_time = 0
        self.all_skipped = []
        self.all_non_skipped = []
        self.to_skip_path = Path(settings.APP_PATH, "tmp", "to_skip")
        self.actioner = SpotifyActioner()
        Path(settings.DATA_PATH, "player_data").mkdir(parents=True, exist_ok = True)
    
    def listen(self):
        self.current_song = self.interface.get_current_song()
        self.previous_song = self.interface.get_current_song()
        self.update_end_time()
        while True:
            if time.time() > self.end_time:
                
                with open(self.to_skip_path, "r") as reader:
                    line = reader.readline()
                if line == "True":
                    self.interface.save_song_features(self.current_song, skip_state="SKIPPED BY ALGORITHM")
                    self.actioner.skip_current_song()
                with open(self.to_skip_path, "w") as writer:
                    writer.write("False")
                self.current_song = self.interface.get_current_song()
                self.previous_song = self.current_song
                self.update_end_time()
                self.all_non_skipped.append(self.previous_song)
                self.previous_song["date_saved"] = str(datetime.now())
                self.interface.save_song_features(self.previous_song,
                                                  "NOT SKIPPEP")
                self.save_all_non_skipped()
                print("not_skipped")
                continue
            else:
                if self.previous_song["id"] != self.current_song["id"]:
                    self.all_skipped.append(self.previous_song)
                    self.save_all_skipped()
                    self.interface.save_song_features(self.previous_song,
                                                      "SKIPPEP")
                    print(f"music skipped {self.previous_song['id']}")
                    self.previous_song = self.current_song
                    self.update_end_time()
                else:
                    self.previous_song = self.current_song

            time.sleep(1)
            self.current_song = self.interface.get_current_song()
            
    def save_all_non_skipped(self):
        self.all_non_skipped = self.all_non_skipped[-50:]
        pd.DataFrame(self.all_skipped).to_csv(Path(settings.DATA_PATH, "player_data",
                                              "non_skipped.csv"), index=False)

    def save_all_skipped(self):
        self.all_skipped = self.all_skipped[-50:]
        pd.DataFrame(self.all_skipped).to_csv(Path(settings.DATA_PATH, "player_data",
                     "skipped.csv"), index=False)

    def update_end_time(self):
        try:
            start_time = time.time()
            length_of_the_song = self.current_song['duration_ms'] / 1000
            self.end_time = start_time + length_of_the_song
        except TypeError:
            print("no song currently playing")
            self.end_time = None

if __name__ == "__main__":
    listener = SKIP_LISTENER()
    listener.listen()
    
    
