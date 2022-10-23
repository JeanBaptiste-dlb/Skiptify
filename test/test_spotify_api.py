import pytest
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE
interface = SPOTIFY_API_INTERFACE()

@pytest.mark.spotify_api_test
def test_get_history():
    interface.get_song_history()


@pytest.mark.spotify_api_test
def test_get_current():
    current_song = interface.get_current_song()
    assert all(
        [
            col
            in [
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
            ]
            for col in current_song.keys()
        ]
    )

def test_save_load_features():
    current_song = interface.get_current_song()
    interface.save_song_features(current_song, "UNKNOWN")
    features = interface.load_song_features(current_song["id"])
    current_song["skip_state"] = "UNKNOWN"
    assert((current_song==features).all())




if __name__ == "__main__":
    test_get_current()
    test_get_history()
    test_save_load_features()
