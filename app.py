from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Was up, Please subscribe, like, and comment on this video, TY!!!'
