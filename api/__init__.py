# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.exceptions import default_exceptions

__version__ = '0.2'

# Setup Flask
app = Flask(__name__)
app.config.from_object('api.config')
app.url_map.strict_slashes = False

# Handle errors in JSON
def json_error(ex):
    return jsonify({
        'success': False,
        'error': {
            'code': ex.code,
            'message': ex.description
        }
    }), ex.code

# Set all exception response codes to return JSON
for code in default_exceptions.keys():
    app.error_handler_spec[None][code] = json_error

# DB setup
db = SQLAlchemy(app)

# db is defined, we can register blueprints now
from api.visits import visits
from api.locations import locations
app.register_blueprint(visits, url_prefix='/visits')
app.register_blueprint(locations, url_prefix='/locations')

# Create tables
db.create_all()
