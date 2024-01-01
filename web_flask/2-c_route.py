#!/usr/bin/python3
"""Starts a Flask application on 0.0.0.0:5000"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns a simple greeting page"""

    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a page containing the string 'HBNB'"""

    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def dear_c(text):
    """Returns a page about C"""

    return ("C {}".format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
