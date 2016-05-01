#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

"""
Generate an authentication token for a sensor. This token is used by the sensor
to send the sensor's data to the API.

After generating a token, you have to place it in the sensor's configuration
file if you want it to send data.
"""

import argparse
import sys
from api import db
from api.tokens.models import Token
from api.locations.models import Location
from sqlalchemy.exc import IntegrityError

def generate_token(name):
    # First create a location
    location = Location(name)
    db.session.add(location)
    try:
        db.session.flush()
    except IntegrityError:
        db.session.rollback()
        sys.stderr.write('Failed to create token: Name {} already exists.\n'.format(name))
        sys.exit(-1)

    # Then generate a token
    token = Token()
    token.location_id = location.id
    db.session.add(token)
    db.session.commit()

    return location

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('name', type=str,
                        help='Name describing a sensor\'s location')
    args = parser.parse_args()

    location = generate_token(args.name)
    print('''=================================
Successfully created token!

Name: {}
Token: {}

Dont forget to save this token in the sensor's configuration file.
================================='''.format(location.name,
                                            location.token.hash))

if __name__ == '__main__':
    main()
