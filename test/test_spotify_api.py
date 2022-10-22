import pytest
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE


@pytest.mark.spotify_api_test
def test_get_history():
    interface = SPOTIFY_API_INTERFACE()
    interface.get_song_history()


@pytest.mark.spotify_api_test
def test_get_current():
    interface = SPOTIFY_API_INTERFACE()
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


if __name__ == "__main__":
    test_get_current()
    test_get_history()
