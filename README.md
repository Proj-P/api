![Project P REST API](https://i.imgur.com/pACOiO6.png)
This repository holds the source code of the RESTful API of [Project P](https://github.com/Proj-P).
This API provides an interface which other applications can use to access
monitored data.

It is written in Python and uses the Flask framework together with a SQLite
database. This is a standalone API, meaning that it does not do any logic such
as detecting toilet usage. It simply manages the data it receives from the
toilet detector service.

# Routes
## Locations
### Get all locations
`GET /locations`

##### Response
```
Status: 200 OK
Content-Type: application/json
```

```
{
  "data": [
    {
      "average_duration": 246.14285714285714,
      "changed_at": "Fri, 17 Jun 2016 03:39:59 GMT",
      "id": 1,
      "name": "Toilet downstairs",
      "occupied": false
    },
    {
      "average_duration": 131.6590909090909,
      "changed_at": "Fri, 17 Jun 2016 10:24:39 GMT",
      "id": 2,
      "name": "Toilet upstairs",
      "occupied": false
    }
  ]
}
```

### Get a location
`GET /locations/:location_id`

##### Response
```
Status: 200 OK
Content-Type: application/json
```

```
{
  "data": {
    "average_duration": 246.14285714285714,
    "changed_at": "Fri, 17 Jun 2016 03:39:59 GMT",
    "id": 1,
    "name": "Toilet downstairs",
    "occupied": false
  }
}
```

### Get all visits by location
`GET /locations/:location_id/visits`

##### Response
```
Status: 200 OK
Content-Type: application/json
```

```
{
  "data": [
    {
      "duration": 189,
      "end_time": "Wed, 22 Jun 2016 14:34:50 GMT",
      "id": 1,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:31:41 GMT"
    },
    {
      "duration": 86,
      "end_time": "Wed, 22 Jun 2016 14:37:48 GMT",
      "id": 2,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:36:22 GMT"
    }
  ]
}
```

### Get all visits by location id in a certain period
`GET /locations/:location_id/visits/:from/:to`

##### Response
```
Status: 200 OK
Content-Type: application/json
```

```
{
  "data": [
    {
      "duration": 189,
      "end_time": "Wed, 22 Jun 2016 14:34:50 GMT",
      "id": 1,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:31:41 GMT"
    },
    {
      "duration": 86,
      "end_time": "Wed, 22 Jun 2016 14:37:48 GMT",
      "id": 2,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:36:22 GMT"
    }
  ]
}
```

### Toggle the status of a location
`PUT /locations/:location_id/toggle`

##### Response
```
Status: 204 No Content
Content-Type: application/json
```

## Visits
### Insert a visit
`POST /visits`

##### Parameters
| Name       | Type | Description             |
|------------|------|-------------------------|
| start_time | int  | Start time in UNIX time |
| end_time   | int  | End time in UNIX time   |

##### Response
```
Status: 201 Created
Content-Type: application/json
```

### Get all visits
`GET /visits`

##### Response
```
Status: 200 OK
Content-Type: application/json
```

```
{
  "data": [
    {
      "duration": 189,
      "end_time": "Wed, 22 Jun 2016 14:34:50 GMT",
      "id": 1,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:31:41 GMT"
    },
    {
      "duration": 86,
      "end_time": "Wed, 22 Jun 2016 14:37:48 GMT",
      "id": 2,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:36:22 GMT"
    }
  ]
}
```

### Get a visit
`GET /visits/:id`

##### Response
```
Status: 200 OK
Content-Type: application/json
```

```
{
  "data": {
      "duration": 189,
      "end_time": "Wed, 22 Jun 2016 14:34:50 GMT",
      "id": 1,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:31:41 GMT"
    }
}
```

### Get all visits in a certain period
`GET /visits/:from/:to`

##### Response
```
Status: 200 OK
Content-Type: application/json
```

```
{
  "data": [
    {
      "duration": 189,
      "end_time": "Wed, 22 Jun 2016 14:34:50 GMT",
      "id": 1,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:31:41 GMT"
    },
    {
      "duration": 86,
      "end_time": "Wed, 22 Jun 2016 14:37:48 GMT",
      "id": 2,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:36:22 GMT"
    }
  ]
}
```

### Get all visits from the past day
`GET /visits/recent`

##### Response
```
Status: 200 OK
Content-Type: application/json
```

```
{
  "data": [
    {
      "duration": 189,
      "end_time": "Wed, 22 Jun 2016 14:34:50 GMT",
      "id": 1,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:31:41 GMT"
    },
    {
      "duration": 86,
      "end_time": "Wed, 22 Jun 2016 14:37:48 GMT",
      "id": 2,
      "location_id": 2,
      "start_time": "Wed, 22 Jun 2016 14:36:22 GMT"
    }
  ]
}
```
