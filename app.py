# __init__.py
import time

from flask import Flask, g, render_template, request
import arrow
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

return app

@app.route('/hello')
def hello_world():
    return 'Please subscribe, like, and comment on this video, TY!!!'

