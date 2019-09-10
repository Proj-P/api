from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

socketio = SocketIO(async_mode='eventlet', cors_allowed_origins='*', engineio_logger=True)
db = SQLAlchemy()


def create_app(debug=False):
    """Create the application"""
    app = Flask(__name__)
    app.debug = debug
    app.url_map.strict_slashes = False
    app.config.from_object(config['development'])

    CORS(app)

    # DB setup
    db = SQLAlchemy(app)

    # db is defined, we can register blueprints now
    from projectp.locations import locations
    from projectp.visits import visits
    from .main import main

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(locations, url_prefix='/locations')
    app.register_blueprint(visits, url_prefix='/visits')

    # Create tables
    db.create_all()

    socketio.init_app(app)
    return app
