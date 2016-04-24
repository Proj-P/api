#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from app import app
import config

app.run(host='0.0.0.0', port=8080, debug=config.DEBUG)
