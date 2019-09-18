from flask import render_template

from . import main


@main.route('/')
def hello_world():
    return render_template('index.html')
