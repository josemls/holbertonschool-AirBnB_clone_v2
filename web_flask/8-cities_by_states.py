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
#!/usr/bin/python3
"""Script that starts Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)

    return render_template('cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ State list """
    states = storage.all("State")
    states = [state for state in states.values()]
    return render_template("8-cities_by_states.html", states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

