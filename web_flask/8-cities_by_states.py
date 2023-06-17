#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models import State


app = Flask(__name__)



@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ State list """
    states = storage.all("State")
    states = [state for state in states.values()]
    return render_template("8-cities_by_states.html", states=states)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
