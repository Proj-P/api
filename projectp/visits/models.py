from datetime import datetime

from projectp import db
from projectp.serializer import Serializer


def _epoch_to_datetime(epoch):
    return datetime.fromtimestamp(float(epoch))


class Visit(db.Model, Serializer):
    __tablename__ = 'visits'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))

    def __init__(self, start_time, end_time, location_id):
        self.start_time = _epoch_to_datetime(start_time)
        self.end_time = _epoch_to_datetime(end_time)
        duration_delta = self.end_time - self.start_time
        self.duration = duration_delta.seconds

        self.location_id = location_id

    def __repr__(self):
        return "<Visit(id='%s', start_time='%s, end_time='%s', duration='%s')>" % (
                   self.id, self.start_time, self.end_time, self.duration)

    # Serialize
    def serialize(self):
        return Serializer.serialize(self)
        # d = Serializer.serialize(self)
        # # Remove filepath from response since its used only internally
        # del d['filepath']
        # return d

