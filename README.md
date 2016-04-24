![Project P REST API](https://i.imgur.com/pACOiO6.png)
This repository holds the source code of the RESTful API of [Project P](https://github.com/Proj-P).
This API provides an interface which other applications can use to access
monitored data.

It is written in Python and uses the Flask framework together with a SQLite
database. This is a standalone API, meaning that it does not do any logic such
as detecting toilet usage. It simply manages the data it receives from the
toilet detector service.
