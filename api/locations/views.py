# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask import jsonify, Blueprint, abort, request
from .models import Location
from api.tokens.models import Token
from api.auth import requires_auth
from api import db, socketio

locations = Blueprint('locations', __name__)

@locations.route('/')
def all():
    """Get all locations"""
    locations = Location.query.all()
    locations = [location.serialize() for location in locations]

    return jsonify(data=locations)

@locations.route('/<int:location_id>')
def status(location_id):
    """Get a location"""
    location = Location.query.get(location_id)

    if location:
        return jsonify(data=location.serialize())

    abort(404, 'Location {} not found.'.format(location_id))

@locations.route('/toggle', methods=['PUT'])
@requires_auth
def update():
    """Toggle the status of a location"""
    hash = request.headers.get('authorization')
    location = Location.query \
        .join(Location.token) \
        .filter_by(hash=hash) \
        .first()

    location.occupied = not location.occupied
    db.session.commit()

    socketio.emit('location', {'occupied': location.occupied}, broadcast=True,
                  namespace='/ws')

    return jsonify(), 204
