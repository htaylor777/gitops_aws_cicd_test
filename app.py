# __init__.py
import time

from flask import Flask, g, render_template, request
import arrow
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('contact.html');   

