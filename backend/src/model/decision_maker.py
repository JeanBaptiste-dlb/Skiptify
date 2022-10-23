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
        self.to_skip_path=Path(settings.APP_PATH, "tmp", "to_skip")


    def decision_maker(self):
        while True:
            next_song = self.interface.get_next_song()
            if next_song != self.next_song:
                self.next_song = next_song
                skip_decision = self.interface.is_song_skipped(next_song["id"])
                # true or false
                with open(self.to_skip_path, "w") as writer:
                    writer.write(str(skip_decision))
                sleep(5)
            


            

    
                
                        
                        
                        
            

                 
            
            




            
                
        sleep(5)
        


