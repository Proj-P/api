# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask import jsonify, Blueprint
from .models import Location
from api.tokens.models import Token
from api import db

locations = Blueprint('locations', __name__)

@locations.route('/')
def all():
    """Get all locations"""
    locations = Location.query.all()
    locations = [location.serialize() for location in locations]

    return jsonify(data=locations, success=True)

@locations.route('/<string:token>/toggle', methods=['PUT'])
def update(token):
    """Update the status of a location"""
    # TODO
    return jsonify(data=token, success=True)
