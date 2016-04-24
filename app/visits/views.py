# -*- coding: utf-8 -*-

# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask import jsonify
from flask import Blueprint

visits = Blueprint('visits', __name__)

@visits.route('/<int:id>', methods=['GET'])
def visit(id):
    return jsonify({
        'id': id
    })
