from flask import Flask, render_template
from radioget import *

app = Flask(__name__)

@app.route('/')
def index():

	url, name, country, language = runRadio()

	return render_template('index.html', url = url, name=name, country=country, language=language)


if __name__ == "__main__":
    app.run()