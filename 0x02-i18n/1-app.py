#!/usr/bin/env python3

'''set up flaska-babel'''

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''configuration class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello():
    '''render template to html file'''
    return render_template('1-index.html')
