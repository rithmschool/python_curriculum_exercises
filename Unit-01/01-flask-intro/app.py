from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/sum')
def sum():
    total = 5+5
    return str(total)
