Backend Engineer Coding Challenge - Django
==========================================

## Problem Statement
Create the back end portion of a simple magazine subscription service where
users can manage subscriptions to available magazines using a REST API.

## Stack
* Python 3.7+
* [Django 3](https://www.djangoproject.com/)
* [Django-REST-Framework](https://www.django-rest-framework.org/)
* SQLite3

## Setup
* Install [Poetry](https://python-poetry.org/docs/#installation)
  ```bash
  # On Linux/MacOS
  curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
  ```
* Install project dependencies
  ```bash
  poetry install
  ```

## Implementation details
* Create Django ORM models in api/models.py
* Create ViewSets and Serializers for each of the models in api/views.py
* Register the viewsets in api/urls.py
* Add tests if any in api/tests.py

## Running / Testing
* poetry run ./manage.py runserver
* poetry run ./manage.py test

## Submitting your results
We are interested in understanding your approach and structuring a
conversation around your implementation.

To prepare and send your submission:
1. Clone this repository and implement your solution
2. Create an archive of the project directory (e.g. - `tar -czf my-name-submission.tar.gz ./my-project-directory`)
3. Email your submission to [engineering@arceo.ai](mailto:engineering@arceo.ai)

