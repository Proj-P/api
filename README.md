![Project P REST API](https://i.imgur.com/pACOiO6.png)
This repository holds the source code of the RESTful API of [Project P](https://github.com/Proj-P).
This API provides an interface which other applications can use to access
monitored data.

It is written in Python and uses the Flask framework together with a SQLite
database. This is a standalone API, meaning that it does not do any logic such
as detecting toilet usage. It simply manages the data it receives from the
toilet detector service.

# API Documentation
See [the wiki](https://github.com/Proj-P/project-p-api/wiki) for a
description of all available routes.

# Prerequisites
[Python](https://www.python.org/downloads/) >= 3.5

# Build and deploy
Deploying the application is easy. A few steps need to be completed.
First, clone the repository and run:
```
$ pip install -r requirements.txt
```
This will install the neccessary packages for the application to run.

Now you need to define the `FLASK_APP`. run the command:
```
$ FLASK_APP=projectp
```

To start the API run:
```
$ python app.py
```

To generate a location, cd to the `scripts/` directory and run
```
$ python generate_token.py <LOCATION_NAME>
```
A prompt will open to ask you some questions and a token will be generated and printed to the console.

If you run in to any errors about your environment variables, you might need to manually set them to `LC_ALL=en_US.utf-8;LANG=en_US.utf-8`.
