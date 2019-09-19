from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import config

socketio = SocketIO(cors_allowed_origins='*', engineio_logger=True)
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

    # The 405
    @app.errorhandler(405)
    def error405(e):
        return "405 Wrong method", 405

    # And the internal server error
    @app.errorhandler(500)
    def error500(e):
        return "500 Internal server error", 500

    # Register blueprints
    app.register_blueprint(main)
    app.register_blueprint(locations, url_prefix='/locations')
    app.register_blueprint(visits, url_prefix='/visits')

    # Create tables
    with app.app_context():
        db.create_all()
        db.session.commit()

    socketio.init_app(app)
    return app
