from flask import render_template, jsonify

from . import main


@main.route('/')
def hello_world():
    return render_template('index.html')

# The 404 response
@main.errorhandler(404)
def page_not_found(error):
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': 'page not found'
        }
    }
    return jsonify(response), 404

# The 405
@main.errorhandler(405)
def error405(e):
    return "405 Wrong method", 405


# And the internal server error
@main.errorhandler(500)
def error500(e):
    return "500 Internal server error", 500
