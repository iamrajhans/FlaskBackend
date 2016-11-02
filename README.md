[![Build Status](https://travis-ci.org/iamrajhans/FlaskBackend.svg?branch=master)](https://travis-ci.org/iamrajhans/FlaskBackend)
# FlaskBackend

## Build backend Using Flask

we will be building a full working backend using flask and postgresql.

## Requirement
- ["Postgresql"](https://www.postgresql.org/docs/9.4/static/tutorial-start.html)

- ["flask"](http://flask.pocoo.org/)

- ["sqlalchemy"](http://www.sqlalchemy.org/)

- ["flask-script"](https://flask-script.readthedocs.io/en/latest/)

- ["flask-migrate"](https://flask-migrate.readthedocs.io/en/latest/)

## Install Virtual Env
`pip install virtualenv`

Then cd to repo's directory and do

`virtualenv .`

`source bin/activate`


## Create db

`createdb flaskmovie`

## Install
Install packages using pip

`pip install -r requirement.txt`

## Run it
Run your app using manager

`python manage.py runserver`

Generate migrations

`python manage.py migrate`

Apply the migration to the database

`python manage upgrade`

To see all the commands that are available run this command

`python manage.py db --help`
