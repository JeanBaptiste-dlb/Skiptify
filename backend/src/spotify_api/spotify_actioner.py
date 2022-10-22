import spotipy
from backend.src.config import settings


class SpotifyActionnner:
    def __init__(self):
        self.scope = settings.scope
        self.token = spotipy.util.prompt_for_user_token(
            settings.USERNAME, settings.scope, client_id=settings.SPOTIPY_CLIENT_ID, client_secret=settings.SPOTIPY_CLIENT_SECRET,
            redirect_uri=settings.SPOTIPY_REDIRECT_URI)
        self.sp = spotipy.Spotify(auth=self.token)
        self.skiped=pd.DataFrame()
        self.played_emtirely=pd.DataFrame()
