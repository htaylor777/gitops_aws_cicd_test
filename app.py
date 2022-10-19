from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Wazzz up my people, get with iti blackness!!'
