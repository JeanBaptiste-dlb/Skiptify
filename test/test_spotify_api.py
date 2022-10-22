import pytest
from backend.src.utils.api_interface import SPOTIFY_API_INTERFACE

@pytest.mark.spotify_api_test
def test_get_history():
    interface = SPOTIFY_API_INTERFACE()
    interface.get_song_history()

