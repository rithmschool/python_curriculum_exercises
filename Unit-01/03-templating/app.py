from flask import Flask, render_template, request, url_for
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# PART 1
@app.route('/person/<name>/<int:age>')
def welcome(name, age):
    return render_template('person.html', name=name, age=age )

# PART 2
@app.route('/calculate')
def calc():
    return render_template('calc.html')

@app.route('/math')
def math():
    calculation = request.args.get('calculation')
    num1 = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))

    if calculation == 'add':
        return str(num1+num2)
    elif calculation == 'subtract':
        return str(num1-num2)
    elif calculation == 'multiply':
        return str(num1*num2)
    try:
        quotient = num1 / num2
    except ZeroDivisionError:
        return "Please do not divide by 0"
    return str(quotient)

# PART 3
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/results')
def results():
  url = 'https://news.google.com'
  keyword = request.args.get('keyword')
  data = requests.get(url)
  soup = BeautifulSoup(data.text, "html.parser")
  titles = soup.select(".titletext")
  articles = [{
    'title': title.text,
    'href': title.parent['href']
  } for title in titles ]

  matching_articles = [
    article 
    for article in articles
    if keyword.lower() in article['title'].lower()
  ]
  return render_template('results.html', articles=matching_articles)
