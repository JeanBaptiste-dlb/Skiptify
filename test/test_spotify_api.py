import pytest
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE


@pytest.mark.spotify_api_test
def test_get_history():
    interface = SPOTIFY_API_INTERFACE()
    interface.get_song_history()


if __name__ == "__main__":
    test_get_history()
