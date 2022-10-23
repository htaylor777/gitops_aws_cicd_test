from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'What is up and down?'

@app.route('/about/'):
    return render_template('about.html')
