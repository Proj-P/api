# -*- coding: utf-8 -*-
# Copyright 2016 Steven Oud. All rights reserved.
# Use of this source code is governed by a MIT-style license that can be found
# in the LICENSE file.

class JSONSerializer:
    def serialize(self):
        """
        Serialize turns an SQLAlchemy result into a JSON serializable object
        so it can be used in jsonify.
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

