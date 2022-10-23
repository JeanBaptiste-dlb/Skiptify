from flask import Flask, redirect, url_for
from utils.frontend_info import df

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return redirect(url_for('welcome'))


@app.route('/welcome')
def welcome():
    data = df.to_dict()
    return {'data': data}, 200  # return data and 200 OK code


if __name__ == '__main__':
    app.run(debug=True)



