from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Wazzz up bebop my jazz people, get with iti blackness!!'
