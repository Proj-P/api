# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.
from flask import jsonify

from projectp import db
from os import urandom
from binascii import hexlify

from projectp.serializer import Serializer


class Token(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.String(32), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    def __init__(self):
        self.hash = self._generate_token(16)

    def __repr__(self):
        return '<Token({location}:{hash})>'.format(location=self.location_id,
                                                  hash=self.hash)

    # def __repr__(self):
    #     return "{'%s':%s}" % (self.location_id, self.hash)

    # Serialize
    def serialize(self):
        # return Serializer.serialize(self)
        d = Serializer.serialize(self)
        # Remove filepath from response since its used only internally
        del d['id']
        return d

        # test

    def _generate_token(self, length):
        return hexlify(urandom(length)).decode('utf-8')
