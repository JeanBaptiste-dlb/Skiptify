from flask import Flask, redirect, url_for
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE
import numpy as np
from flask_cors import CORS
import csv
import pandas as pd

app = Flask(__name__)
CORS(app)
app.debug = True
sp = SPOTIFY_API_INTERFACE()
sp.get_current_song()


def skipped_song_list():
    df = pd.read_csv('../../data/player_data/skipped.csv')
    skipped_song_list = pd.DataFrame(index=df['id'].to_list())
    for id in df['id']:
        song_info = sp.get_track_metadata(id)
        skipped_song_list.loc[id] = song_info
    return skipped_song_list


@app.route('/')
def index():
    return redirect(url_for('current_info'))


@app.route('/current_info')
def current_info():
    data = sp.get_metadata()
    #skipped_songs = skipped_song_list()
    if data is not None:
        dict = data.to_dict()

    else:
        dict = pd.Series()
    return dict, 200  # return data and 200 OK code

if __name__ == '__main__':
    app.run(debug=True)
