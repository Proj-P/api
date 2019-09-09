# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask import request, jsonify
from functools import wraps
from projectp.tokens.models import Token


def verify_token(hash):
    """
    Looks up given token in the database and verifies if it exists and is valid
    """
    token = Token.query.filter_by(hash=hash.replace('Bearer ', '')).first()
    return token is not None


def requires_auth(f):
    @wraps(f)
    def _require_auth(*args, **kwargs):
        auth = request.headers.get('authorization')
        if not auth or not verify_token(auth):
            return jsonify(message='Unauthorized!', code=401), 401
        return f(*args, **kwargs)
    return _require_auth
