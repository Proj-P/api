# -*- coding: utf-8 -*-

# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

from app.visits import visits

# Flask setup
app = Flask(__name__)
app.register_blueprint(visits, url_prefix='/visits')
app.config.from_object('config')

# Handle 404s
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'message': str(error)
    }), 404

# DB setup
db = SQLAlchemy(app)
db.create_all()
