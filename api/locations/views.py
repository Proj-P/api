# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask.json import dumps
from flask import jsonify, Blueprint, abort, request
from .models import Location
from api.visits.models import Visit
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

@locations.route('/<int:location_id>/visits')
def visits(location_id):
    """Get a location"""
    visits = Visit.query.filter_by(location_id=location_id).all()
    visits = [visit.serialize() for visit in visits]

    if visits:
        return jsonify(data=visits)

    abort(404, 'No visits found.')


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

    socketio.emit('location', {'location': dumps(location.serialize())},
                  broadcast=True)

    return jsonify(), 204
