import pandas as pd

def add_song_to_db(song_info: pd.Series) -> None:
    """
    add the given song to the database

    song_info: dataframe with columns mood, ... and if the song was skipped.
    """
