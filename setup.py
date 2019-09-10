from setuptools import setup

setup(
    name='project-p-api',
    description='This API is part of Project P and provides an interface which other applications can use to access monitored data.',
    url='https://github.com/Proj-P/project-p-api',
    license='MIT',
    author='Steven Oud, Teun Kelting',
    author_email='soud@protonmail.com, teun@tjuna.com',
    version='2.0',
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask-socketio',
        'eventlet',
        'flask_cors',
        'flask_wtf',
        'wtforms',
        'sqlalchemy',
        'werkzeug'
    ],
    entry_points={
        'console_scripts': [
            'pp-generate-token = script.generate_token:main'
        ]
    }
)
