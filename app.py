# __init__.py
import time

from flask import Flask 
import render_template
import request
import arrow
import requests
app = Flask(__name__)

@app.route('/')
def this_index():
    return render_template('contact.html')
return app

@app.route('/hello')
def hello_world():
    return 'Please subscribe, like, and comment on this video, TY!!!'

