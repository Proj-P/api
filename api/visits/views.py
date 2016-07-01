# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask.json import dumps
from flask import jsonify, Blueprint, abort, request
from datetime import datetime, timedelta
from api import db, socketio
from api.auth import requires_auth
from api.locations.models import Location
from .models import Visit
from .forms import VisitForm, DateForm

visits = Blueprint('visits', __name__)

@visits.route('/', methods=['POST'])
@requires_auth
def insert():
    """Insert a visit"""
    form = VisitForm()

    if not form.validate():
        return jsonify(errors=form.errors), 400

    # Get location based on token
    hash = request.headers.get('authorization')
    location = Location.query \
        .join(Location.token) \
        .filter_by(hash=hash) \
        .first()

    visit = Visit(request.form.get('start_time'), request.form.get('end_time'),
                  location.id)
    db.session.add(visit)

    socketio.emit('visit', dumps(visit.serialize()), broadcast=True)

    # Recalculate average
    location.calculate_average()

    db.session.commit()

    return jsonify(), 201, {'Location': '/visits/' + str(visit.id)}


@visits.route('/')
def all():
    """Get all visits"""
    visits = Visit.query.all()
    visits = [visit.serialize() for visit in visits]

    return jsonify(data=visits)

@visits.route('/recent')
def recent():
    """Get all visits from the past day"""
    interval = datetime.now() - timedelta(days=1)
    visits = Visit.query                      \
        .filter(Visit.start_time >= interval) \
        .order_by(Visit.start_time)           \
        .all()
    visits = [visit.serialize() for visit in visits]

    return jsonify(data=visits)

@visits.route('/<start>/<end>')
def visits_range(location_id, start, end):
    """Get all visits by a certain period"""
    form = DateForm(MultiDict(request.view_args))

    if not form.validate():
        return jsonify(errors=form.errors), 400

    visits = Visit.query                              \
        .filter(Visit.start_time.between(start, end)) \
        .order_by(Visit.start_time)                   \
        .all()
    visits = [visit.serialize() for visit in visits]

    return jsonify(data=visits)


@visits.route('/<int:id>')
def visit(id):
    """Get a visit by id"""
    visit = Visit.query.get(id)

    if visit:
        return jsonify(data=visit.serialize())

    abort(404, 'Visit "{}" not found.'.format(id))
