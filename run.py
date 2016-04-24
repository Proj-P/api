#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

import time
from flask import jsonify
from config import HOST, PORT
from api import app

start_time = time.time()

@app.route('/')
def index():
    return jsonify({
        'uptime': time.time() - start_time
    })

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
