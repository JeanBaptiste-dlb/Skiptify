from backend.src.config import settings
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE
import pandas as pd


class DecisionLoop:
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
        self.next_song = None
        Path(settings.APP_PATH, "", "")


    def decision_maker(self):
        while True:
            next_song = self.interface.get_next_song()
            if next_song != self.next_song:
                self.next_song = next_song
                skipped = self.interface.is_song_skipped(song_id)
                # true or false
                if skipped:
                    with open
                 
            
            




            
                
        sleep(5)
        


