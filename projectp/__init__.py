from flask import Flask, jsonify, Blueprint
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(config['development'])

CORS(app)

socketio = SocketIO(app)

# DB setup
db = SQLAlchemy(app)

# db is defined, we can register blueprints now
from projectp.locations import locations
from projectp.visits import visits

# Register blueprints
app.register_blueprint(locations, url_prefix='/locations')
app.register_blueprint(visits, url_prefix='/visits')
errors = Blueprint('errors', __name__)

# Create tables
db.create_all()


@app.route('/')
def hello_world():
    return 'Hello World!'


# Some error handling
@errors.app_errorhandler(Exception)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = error.status_code
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code


# The 404 response
@app.errorhandler(404)
def page_not_found(error):
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': 'page not found'
        }
    }
    return jsonify(response), 404


@app.errorhandler(404)
def page_not_found(e):
    return "404 not found", 404


# The 405
@app.errorhandler(405)
def error405(e):
    return "405 Wrong method", 405


# And the internal server error
@app.errorhandler(500)
def error500(e):
    return "500 Internal server error", 500


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
