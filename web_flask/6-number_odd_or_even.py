#!/usr/bin/python3
"""Script that start a flask application."""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Return a given message."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def message1():
    """Return a given message."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def formated_text(text):
    """Format a given text."""
    new = text.replace('_', " ")
    return "C" + " " + new


@app.route('/python/', defaults={'text': "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def another_string(text):
    """Return a given message."""
    new = text.replace('_', ' ')
    return "Python" + ' ' + new


@app.route('/number/<int:n>', strict_slashes=False)
def just_a_number(n):
    """Return a string if the value is an integer."""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_html(n):
    """Give value to a variable in the html."""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """Give value to a variable in the html."""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
