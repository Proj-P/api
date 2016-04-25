# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from flask_wtf import Form
from wtforms import IntegerField
from wtforms.validators import InputRequired

class VisitForm(Form):
    start_time = IntegerField('start_time', [InputRequired()])
    end_time = IntegerField('end_time', [InputRequired()])
