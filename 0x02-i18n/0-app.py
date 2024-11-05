#!/usr/bin/env python3

'''basic flask setup'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hell():
    '''
    render message to the client
    '''
    return render_template('0-index.html')
