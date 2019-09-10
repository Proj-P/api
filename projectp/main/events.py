from projectp import socketio


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    print('SocketIO error: ', e)


@socketio.on('connect')
def connect():
    print('connected a SocketIO client')
