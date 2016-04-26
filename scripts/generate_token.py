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
from sqlalchemy.exc import IntegrityError

def generate_token(name):
    token = Token(name)
    db.session.add(token)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        sys.stderr.write('Failed to create token: Name {} already exists.\n'.format(name))
    finally:
        db.session.close()
        sys.exit(-1)

    return token

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-n', '--name', type=str, required=True,
                        help='Name describing a sensor\'s location')
    args = parser.parse_args()

    token = generate_token(args.name)
    print('''
Successfully created token!

Name: {}
Token: {}

Dont forget to save this token in the sensor's configuration file.
'''.format(token.name, token.token.decode('utf-8')))

if __name__ == '__main__':
    main()
