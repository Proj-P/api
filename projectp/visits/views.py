from datetime import datetime, timedelta

from flask import jsonify, Blueprint, request, render_template
from werkzeug.datastructures import MultiDict

from projectp import db, socketio
from projectp.auth import requires_auth
from projectp.locations.models import Location
from projectp.visits.forms import VisitForm, DateForm
from .models import Visit

visits = Blueprint('visits', __name__)


@visits.route('/')
def all():
    """Get all visits"""
    visits = Visit.query.all()

    return jsonify(Visit.serialize_list(visits))


@visits.route('/', methods=['POST'])
@requires_auth
def insert():
    """Insert a visit"""
    print(request.form)

    if request.method == 'POST':

        # Get location based on token
        hash = request.headers.get('authorization')
        location = Location.query \
            .join(Location.token) \
            .filter_by(hash=hash.replace('Bearer ', '')) \
            .first()

        visit = Visit(request.form['start_time'], request.form['end_time'], location.id)

        db.session.add(visit)

        socketio.emit('visit', jsonify(visit.serialize()), broadcast=True)

        # Recalculate average
        location.calculate_average()
        # Save in DB
        db.session.commit()

        # Return JSON 201 successfully created response
        return jsonify(
            message='Visit {} has been uploaded successfully.'.format(visit.id),
            visit=visit.serialize(),
            code=201
        ), 201

    # return jsonify(message='Form errors!', error=form.errors, code=400), 400

    # return render_template('visit.html', form=form)

    # return jsonify(), 201, {'Location': '/visits/' + str(visit.id)}


@visits.route('/recent')
def recent():
    """Get all visits from the past day"""
    interval = datetime.now() - timedelta(days=1)
    visits = Visit.query \
        .filter(Visit.start_time >= interval) \
        .order_by(Visit.start_time) \
        .all()
    # visits = [visit.serialize() for visit in visits]

    return jsonify(Visit.serialize_list(visits))


@visits.route('/<start>/<end>')
def visits_range(location_id, start, end):
    """Get all visits by a certain period"""
    form = DateForm(MultiDict(request.view_args))

    if not form.validate():
        return jsonify(message='Form errors!', error=form.errors, code=400), 400

    visits = Visit.query \
        .filter(Visit.start_time.between(start, end)) \
        .order_by(Visit.start_time) \
        .all()

    return jsonify(Visit.serialize_list(visits))


@visits.route('/<int:id>')
def visit(id):
    """Get a visit by id"""
    visit = Visit.query.get(id)

    if visit:
        return jsonify(visit.serialize())

    return jsonify(message='Visit {} not found.'.format(id), code=404), 404
