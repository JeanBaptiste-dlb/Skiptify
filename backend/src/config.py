import os

from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

from datetime import datetime
import spotipy
import os
from dotenv import dotenv_values
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict

from datetime import datetime
from pydantic import BaseSettings, root_validator


class Settings(BaseSettings):
    """
    Settings class for application settings and secrets management
    Official documentation on pydantic settings management:
    - https://pydantic-docs.helpmanual.io/usage/settings/
    """

    # Set the application variables
    APP_NAME: str = "Test"
    # if you want to test gunicorn the below environment variabile must be False
    DEBUG_MODE: str = "True"
    VERBOSITY: str = "DEBUG"

    # Application Path
    APP_PATH: str = os.path.abspath(".")
    DATA_PATH: str = os.path.join(APP_PATH, "app", "data")


    #-----------------
    # Token for getting song's info from Spotify
    USERNAME=""
    SPOTIPY_CLIENT_ID=""
    SPOTIPY_CLIENT_SECRET=""
    SPOTIPY_REDIRECT_URI="https://example.com/callback"

    # Token for getting lyrics from Genius website - Rangsiman
    token=""
    #-----------------

    scope = 'user-read-currently-playing'

    # To connect succesfully you need to provide your own Spotify Credentials
    # You can do this signing up in https://developer.spotify.com/ and creating a new app.
    token = spotipy.util.prompt_for_user_token(
        USERNAME, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI)


def env_load(env_file: str) -> Settings:
    """
    If you want to generate settings with a specific .env file.
    Be carefull: you have to insert only the env that are in the config.
    Look into official technical documentation for more information about the variables.

    Args:
        env_file (str): The path to the .env file. (with the name)

    Returns:
        Settings: The settings object with the .env file loaded.
    """
    try:
        # get the dotenv file values into an OrderedDict
        env_settings = dotenv_values(env_file)
        # convert to normal dict
        env_settings = dict(env_settings)
        # define and create the new object
        settings = Settings(**env_settings)
        return settings
    except Exception as message:
        print(f"Error: impossible to read the env: {message}")
        return None
# cache system to read the settings without everytime read the .env file
@lru_cache()
def get_settings(settings: Settings = None, env_file: str = None, **kwargs) -> Settings:
    """
    Function to get the settings object inside the config.
    This function use lru_cache to cache the settings object and avoid to read everytime the .env file from disk (much more faster)

    Args:
        settings (Settings, optional): The settings object to use. Defaults to None.
    Returns:
        Settings: The settings object.
    """
    # define the new settings
    try:
        if not settings:
            if env_file:
                # check if env file existing
                if not Path(env_file).exists():  # nocov
                    settings = None
                    raise ValueError(f"Config file {env_file} does not exist.")
                else:
                    settings = env_load(env_file)
            else:
                settings = Settings(**kwargs)

        return settings
    except Exception as message:
        print(f"Error: impossible to get the settings: {message}")
        return None


# # define the settings (use the env file if it's used)
env_file = os.environ.get("ENV_FILE", None)
settings = get_settings(env_file=env_file)
