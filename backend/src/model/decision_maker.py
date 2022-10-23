from backend.src.config import settings
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE
import pandas as pd
from pathlib import Path
import time

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
        self.to_skip_path=Path(settings.DATA_PATH, "tmp", "to_skip")
        self.to_skip_path.mkdir(parents=True, exist_ok= True)

    def decision_maker(self):
        while True:
            next_song = self.interface.get_next_song()
            if next_song != self.next_song:
                print("wrote a decision")
                self.next_song = next_song
                skip_decision = self.interface.is_song_skipped(next_song)
                # true or false
                with open(Path(self.to_skip_path, "skip_decision.txt"), "w") as writer:
                    writer.write(str(skip_decision))
            time.sleep(5)

def main():
    loop=DecisionLoop()
    loop.decision_maker()

if __name__=="__main__":
    main()
            

    
                        
                        
                        
            

                 
            
    


