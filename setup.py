#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

import re
import ast
from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('api/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='project-p-api',
    version=version,
    description='This API is part of Project P and provides an interface which'
                ' other applications can use to access monitored data.',
    url='https://github.com/Proj-P/project-p-api',
    license='MIT',
    author='Steven Oud',
    author_email='soud@protonmail.com',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'gevent==1.1.1',
        'Flask==0.11',
        'Flask-SocketIO==2.4',
        'Flask-SQLAlchemy==2.1',
        'Flask-WTF==0.12',
        'itsdangerous==0.24',
        'MarkupSafe==0.23',
        'SQLAlchemy==1.0.12',
        'Werkzeug==0.11.10',
        'WTForms==2.1'
    ],
    entry_points = {
        'console_scripts': [
            'pp-run-server = api.run:main',
            'pp-generate-token = scripts.generate_token:main'
        ]
    }
)
