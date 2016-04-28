# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

from api import db
from api.models import JSONModel
from datetime import datetime

class Visit(JSONModel):
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    def __init__(self, start_time, end_time):
        self.start_time = self._epoch_to_datetime(start_time)
        self.end_time = self._epoch_to_datetime(end_time)
        duration_delta = self.end_time - self.start_time
        self.duration = duration_delta.seconds

    def __repr__(self):
        return 'Visit<{id} {start_time}-{end_time}>'.format(
            id=self.id,
            start_time=self.start_time,
            end_time=self.end_time,
        )

    def _epoch_to_datetime(self, epoch):
        return datetime.fromtimestamp(float(epoch))
