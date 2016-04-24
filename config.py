# -*- coding: utf-8 -*-

# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

import os

# Debug state
DEBUG = True

# Application root directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Database (sqlite) configuration
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True
