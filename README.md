# Career Registration Project

***

This repository is intended for the development of a CRUD system for career management.

## Table of Contents

***

1. [Technologies](#technologies)
2. [Installation on Windows](#installation)
3. [Endpoints](#endpoints)

## Technologies

***
A list of technologies used within the project:

* [Python](https://www.python.org): Version 3.11
* [Django](https://www.djangoproject.com): Version 5.0.2
* [Django Rest Framework](https://www.django-rest-framework.org): Version 3.0.5

## Installation

***

```bash
# Clone this repo
$ git clone git@github.com:jeniferss/CareerRegistrationProject.git

# Go into the repo app
$ cd CareerRegistrationProject

# Create a virtual environment
$ python -m venv venv

# Activate your virtual environment
$ venv\Scripts\activate

# Install the project requirements
$ pip install -r requirements.txt

# Run Django migrations
$ python manage.py migrate

# Run Django server
$ python manage.py runserver

# Server will start at http://localhost:8000
```

## Endpoints

***

*base_url*: `http://localhost:8000`

### List all careers

url: `{base_url}/careers/`

method: `GET`

status_code: `200 OK`

```json
{
  "count": "number",
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": "number",
      "created_datetime": "datetime",
      "username": "string",
      "title": "string",
      "content": "string",
      "author_ip": "string"
    }
  ]
}

```

### Show a career

url: `{base_url}/careers/{carrer_id}/`

method: `GET`

status_code: `200 OK`

```json
{
  "id": "number",
  "created_datetime": "datetime",
  "username": "string",
  "title": "string",
  "content": "string",
  "author_ip": "string"
}
```

status_code: `404 NOT FOUND`

```json
{
  "detail": "Not found."
}
```

### Create a career

url: `{base_url}/careers/`

method: `POST`

body:

```json
{
  "username": "string",
  "title": "string",
  "content": "string"
}

```

status_code: `200 OK`

```json
{
  "id": "number",
  "created_datetime": "datetime",
  "username": "string",
  "title": "string",
  "content": "string",
  "author_ip": "string"
}
```

### Update a career

url: `{base_url}/careers/{carrer_id}/`

method: `PATCH`

body:

```json
{
  "title": "string",
  "content": "string"
}

```

status_code: `200 OK`

```json
{
  "id": "number",
  "created_datetime": "datetime",
  "username": "string",
  "title": "string",
  "content": "string",
  "author_ip": "string"
}
```

status_code: `405 METHOD NOT ALLOWED`

```json
{
  "detail": "The PATCH method is not allowed without providing an ID in the path."
}
```

status_code: `404 NOT FOUND`

```json
{
  "detail": "Not found."
}
```

### Delete a career

url: `{base_url}/careers/{carrer_id}/`

method: `DELETE`

status_code: `204 NO CONTENT`

```json

```

status_code: `405 METHOD NOT ALLOWED`

```json
{
  "detail": "The DELETE method is not allowed without providing an ID in the path."
}
```

status_code: `404 NOT FOUND`

```json
{
  "detail": "Not found."
}
```
