# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from datetime import datetime
from api.models import JSONSerializer
from api import db

class Location(db.Model, JSONSerializer):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    occupied = db.Column(db.Boolean, nullable=False, default=False)
    changed_at = db.Column(db.DateTime, default=None, onupdate=datetime.now())

    token = db.relationship('Token', backref='locations', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Location<{}>'.format(self.name)
