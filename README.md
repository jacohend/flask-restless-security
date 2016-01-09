[![Build Status](https://travis-ci.org/graup/flask-restless-security.svg?branch=master)](https://travis-ci.org/graup/flask-restless-security)

This is a starting point for a [Flask](http://flask.pocoo.org/) website + API using:

- [Flask-Restless](https://flask-restless.readthedocs.org/en/latest/) (API)
- [Flask-Security](https://pythonhosted.org/Flask-Security/) (Authentication)
- [Flask-JWT](https://pythonhosted.org/Flask-JWT/) (API authentication)
- [Flask-Admin](http://flask-admin.readthedocs.org/en/latest/) (Admin views)
- [SQLAlchemy](http://www.sqlalchemy.org/) (ORM)

Plus stubs for

- Templates
- Testing

Github user "graup" got the basic idea from Nic:
http://stackoverflow.com/a/24258886/700283

Setup
=====

- Setup a postgres database, or edit config.py with your own db URI
- Build docker image from dockerfile
- Run docker container with 'docker run -e DB_USER=user -e DB_PASS=pass -e DB_HOST=host -e DB_NAME=name -e SERVER_ENV=Production|Development|Testing -e APP_NAME=app -e SECRET_KEY=key -e SECURITY_PASSWORD_SALT=salt  <image name>'

**Website**

- Access site at /. Not much there, just a basic example for logging in

**Admin**

- Access admin at /admin

**API auth**

- POST /api/v1/auth {'username': '', 'password': ''}
- Returns JSON with {'access_token':''}  
- Then request from API using header 'Authorization: JWT $token'

**Tests**

- Run tests using `python test.py`
