# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from api import db
from os import urandom
from binascii import hexlify

class Token(db.Model):
    __tablename__ = 'tokens'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    token = db.Column(db.String(32), nullable=False)

    def __init__(self, name):
        self.name = name
        self.token = self._generate_token(16)

    def _generate_token(self, length):
        return hexlify(urandom(length))
