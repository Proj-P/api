# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask import jsonify, Blueprint, abort, request
from datetime import datetime, timedelta
from api.visits.models import Visit

visits = Blueprint('visits', __name__)

@visits.route('/', methods=['POST'])
def insert():
    """Insert a visit"""
    return 'TODO'

@visits.route('/')
def all():
    """Get all visits and filter by offset and limit"""
    offset = request.args.get('offset') or 0
    limit = request.args.get('limit') or 0
    visits = Visit.query.order_by(Visit.start_time)\
        .limit(limit)\
        .offset(offset)\
        .all()

    return jsonify(data=visits, success=True)

@visits.route('/recent')
def recent():
    """Get all visits from the past day"""
    interval = datetime.now() - timedelta(days=1)
    visits = Visit.query.filter(Visit.start_time >= interval).order_by(Visit.start_time).all()

    return jsonify(data=visits, success=True)

@visits.route('/<int:id>')
def visit(id):
    """Get a visit by id"""
    visit = Visit.query.get(id)

    if visit:
        return jsonify(data=visit, success=True)

    abort(404, 'Visit "{}" not found'.format(id))
