from flask import Flask, redirect, url_for
from backend.src.spotify_api.api_interface import SPOTIFY_API_INTERFACE

app = Flask(__name__)
app.debug = True

sp = SPOTIFY_API_INTERFACE()
sp.get_current_song()


@app.route('/')
def index():
    return redirect(url_for('current_info'))


@app.route('/current_info')
def current_info():
    data = sp.get_current_song()
    dict = data.to_dict()
    return {'data': dict}, 200  # return data and 200 OK code

@app.route('/skipped_songs')
def skipped_song():
    data = sp.get_current_song()
    dict = data.to_dict()
    return {'data': dict}, 200  # return data and 200 OK code

if __name__ == '__main__':
    app.run(debug=True)



