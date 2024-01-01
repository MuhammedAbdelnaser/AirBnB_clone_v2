#!/usr/bin/python3
""" strats a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return ("HBNB")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
