from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/demo2')
def demo2():
    return render_template('demo2.html') 

@app.route('/demo3')
def demo3():
    return render_template('demo3.html')
    
@app.route('/demo4')
def demo4():
    return render_template('demo4.html')  

@app.route('/home')
def home():
    return render_template('index.html')      
    
