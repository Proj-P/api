from flask import jsonify, Blueprint, request, json
from werkzeug.datastructures import MultiDict

from projectp import socketio

from projectp import db
from projectp.auth import requires_auth
from projectp.visits.forms import DateForm
from projectp.visits.models import Visit
from .models import Location

locations = Blueprint('locations', __name__)


@locations.route('/')
def all():
    """Get all locations"""
    locations = Location.query.all()

    return jsonify(Location.serialize_list(locations))


@locations.route('/<int:location_id>')
def status(location_id):
    """Get a location"""
    location = Location.query.get(location_id)

    if location:
        return jsonify(location.serialize())

    return jsonify(message='Location {} not found.'.format(location_id), code=404), 404


@locations.route('/<int:location_id>/visits')
def visits(location_id):
    """Get all visits by location id"""
    visits = Visit.query.filter_by(location_id=location_id).all()
    print(visits)

    if visits:
        return jsonify(Visit.serialize_list(visits))

    if not len(visits):
        return jsonify({})

    return jsonify(message='Something went wrong'.format(location_id), code=400), 400


@locations.route('/<int:location_id>/visits/<start>/<end>')
def visits_range(location_id, start, end):
    """Get all visits by location id in a certain period"""
    form = DateForm(MultiDict(request.view_args))

    if not form.validate():
        return jsonify(message='Form errors!', error=form.errors, code=400), 400

    visits = Visit.query \
        .filter_by(location_id=location_id) \
        .filter(Visit.start_time.between(start, end)) \
        .order_by(Visit.start_time) \
        .all()

    return jsonify(visits.serialize_list())


@locations.route('/status', methods=['PUT'])
@requires_auth
def set_status():
    """Set the status of a location"""
    occupied = request.form.get('occupied')

    if occupied not in ['true', 'false']:
        return jsonify(message='Occupied should be either true or false, not {}.'.format(occupied), code=400), 400

    h = request.headers.get('Authorization')
    location = Location.query \
        .join(Location.token) \
        .filter_by(hash=h.replace('Bearer ', '')) \
        .first()

    # convert true and false to True and False
    location.occupied = True if occupied == 'true' else False

    db.session.commit()

    i = location.serialize()
    socketio.emit('location', json.dumps(i), broadcast=True)
    # socketio.emit('test', json.dumps(i), broadcast=True, room='test')

    return jsonify(message='Location {} updated succesfully.'.format(location.id), code=200, location=location.serialize()), 200

