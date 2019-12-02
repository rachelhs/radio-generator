from flask import Flask, render_template, request
from radioget import *

app = Flask(__name__)

@app.route('/')
def index():
	url, name, country, language = runRadio()
	return render_template('index.html', url = url, name=name, country=country, language=language)

@app.route('/10seconds')
def tenSeconds():
	url, name, country, language = runRadio()
	return render_template('10seconds.html', url = url, name=name, country=country, language=language)

@app.route('/1minute')
def oneMinute():
	url, name, country, language = runRadio()
	return render_template('1minute.html', url = url, name=name, country=country, language=language)

@app.route('/10minutes')
def tenMinutes():
	url, name, country, language = runRadio()
	return render_template('10minutes.html', url = url, name=name, country=country, language=language)

@app.route('/1hour')
def oneHour():
	url, name, country, language = runRadio()
	return render_template('1hour.html', url = url, name=name, country=country, language=language)

if __name__ == "__main__":
    app.run()