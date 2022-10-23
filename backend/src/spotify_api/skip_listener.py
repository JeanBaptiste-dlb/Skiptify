import pandas as pd
import spotipy
from backend.src.config import settings
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE
import spotipy.util as util
import json
import numpy as np
from pathlib import Path
import time


class SKIP_LISTENER:
    def __init__(self):
        self.scope = settings.scope
        self.skiped = pd.DataFrame()
        self.played_emtirely = pd.DataFrame()
        self.interface = SPOTIFY_API_INTERFACE()
        self.current_song = None
        self.previous_song = None
        self.end_time = 0
        self.all_skiped = []
        self.all_non_skiped = []
        self.end_time
    
    def listen(self):
        self.current_song = self.interface.get_current_song()
        self.previous_song = self.interface.get_current_song()
        self.calc_end_time()
        while True:
            if time.time() < self.endtime:
                if self.previous_song["id"] != self.current_song["id"]:
                    self.all_skiped.append(self.previous_song)
                    self.interface.save_song_features(self.previous_song,
                                                      "SKIPPEP")
                    print(f"music skipped {self.previous_song['id']}")
                    self.previous_song = self.current_song
            else:
                self.previous_song
                self.all_non_skiped.append(self.previous_song)
                self.save_all_non_skipped()
                print("not_skipped")
                self.current_song = self.interface.get_current_song()
                self.calc_end_time()
            
            time.sleep(5)

    def save_all_non_skipped(self):
        self.all_non_skipped = self.all_non_skipped[-50:]
        pd.to_csv(self.all_non_skipped, Path(settings.DATA_PATH, "player_data", "non_skipped.csv"))

    def save_all_skipped(self):
        self.all_skipped = self.all_skipped[-50:]
        pd.to_csv(self.all_skipped, Path(settings.DATA_PATH, "player_data",
                  "skipped.csv"))

    def calc_end_time(self):
        try:
            start_time = time.time()
            length_of_the_song = self.current_song['duration_ms'] / 1000
            self.endtime = start_time + length_of_the_song
        except TypeError:
            print("no song currently playing")
            self.endtime = None

if __name__ == "__main__":
    listener = SKIP_LISTENER()
    listener.listen()
    
    
