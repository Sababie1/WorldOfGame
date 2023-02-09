from flask import Flask, render_template, request
from pathlib import Path
from lxml import html
import requests
import MainScores

app = Flask(__name__)

app = Flask(__name__)


# Creating a route that has both GET and POST request methods
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':

    return render_template('score.html')


# Initiating the application
if __name__ == '__main__':
    # Running the application and leaving the debug mode ON
    app.run(debug=True)