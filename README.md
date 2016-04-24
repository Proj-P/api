![Project P REST API](https://photos-2.dropbox.com/t/2/AACuqeyRCZHBCJGfTdgbwocBeVkksLJ6J9PF4SRVZxvpzA/12/59610199/png/32x32/1/1461470400/0/2/projectp-icon-restapi.png/EPaojC4Y8sgrIAIoAg/PedOhRk2RHqLlWvBIGC2GUlL62PrJd56HYRLuSBFC3M?size_mode=3&size=1280x960)
This repository holds the source code of the RESTful API of [Project P](https://github.com/Proj-P).
This API provides an interface which other applications can use to access
monitored data.

It is written in Python and uses the Flask framework together with a SQLite
database. This is a standalone API, meaning that it does not do any logic such
as detecting toilet usage. It simply manages the data it receives from the
toilet detector service.
