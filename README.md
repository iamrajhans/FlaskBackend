# FlaskBackend

##Build backend Using Flask

we will building a full working backend using flask and the database we will be
using is postgresql

##Requirement
- ["Postgresql"](https://www.postgresql.org/docs/9.4/static/tutorial-start.html)

- ["flask"](http://flask.pocoo.org/)

- ["sqlalchemy"](http://www.sqlalchemy.org/)

- ["flask-script"](https://flask-script.readthedocs.io/en/latest/)

- ["flask-migrate"](https://flask-migrate.readthedocs.io/en/latest/)

##Install
Install packages using pip

`pip install -r requirement.txt`

##Run it
Run your app using manager

`python manage.py runserver`

To create migration repository 

`python manage.py db init`

Generate an initial migration 

`python manage.py migrate`

Apply the migration to the database

`python manage upgrade`

To see all the commands that are available run this command

`python manage.py db --help`


##Authentication

For user login use ["flask-bcrypt"](https://flask-bcrypt.readthedocs.io/en/latest/)
["hashlib"](https://docs.python.org/2/library/hashlib.html)
["base64"](https://docs.python.org/2/library/base64.html)

##Note
- Do your work in ["virtualenev"](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
