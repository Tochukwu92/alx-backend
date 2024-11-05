#!/usr/bin/env python3

'''set up flaska-babel'''

from flask import Flask, render_template, request
from flask_babel import Babel, _


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
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    '''get best match language'''
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )
