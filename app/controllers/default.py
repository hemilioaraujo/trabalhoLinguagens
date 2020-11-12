from flask.globals import request
from app import app
from flask import render_template
from app.controllers.functions import getTokens


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        tokens = getTokens(request.form['expression'])
    else:
        tokens = None
    return render_template('index.html', tokens=tokens)