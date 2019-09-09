import datetime

from projectp import db
from projectp.serializer import Serializer
from projectp.visits.models import Visit


class Location(db.Model, Serializer):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    occupied = db.Column(db.Boolean, nullable=False, default=False)
    changed_at = db.Column(db.DateTime, default=None, onupdate=datetime.datetime.now())
    average_duration = db.Column(db.Integer, default=0)

    token = db.relationship('Token', backref='locations', uselist=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Location(id='%s', name='%s', occupied='%s', changed_at='%s', " \
               "average_duration='%s')>" % (
                   self.id, self.name, self.occupied, self.changed_at, self.average_duration)

    # Serialize
    def serialize(self):
        # return Serializer.serialize(self)
        d = Serializer.serialize(self)
        # Remove filepath from response since its used only internally
        del d['token']
        return d

    def calculate_average(self):
        visits = Visit.query.with_entities(Visit.duration).all()
        # Flatten list
        visits = list(sum(visits, ()))

        self.average_duration = sum(visits) / len(visits)
