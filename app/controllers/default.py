from flask.globals import request
from app import app
from flask import render_template
from app.controllers.token import getTokens
from app.controllers.grammar import getGrammar


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        tokens = getTokens(request.form['expression'])
        grammar = getGrammar(tokens)
    else:
        tokens = None
        grammar = None
    return render_template('index.html', tokens=tokens, grammar=grammar)