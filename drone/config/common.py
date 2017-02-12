#include your common config to your app
import logging

SQLALCHEMY_TRACK_MODIFICATIONS = False

APP_LOG_LEVEL = logging.INFO
SECRET_KEY ='secret key'

DEBUG = True
#------- Database URI ----------#
SQLALCHEMY_DATABASE_URI= 'postgresql://username:password@localhost:5432/db_name'

#-------- Sentry ------#
DSN_SENTRY ='https://8bde72b5d31d49b497f1e49226ae0f96:71b0bc035d684846803e5e6ef725ca96@app.getsentry.com/94768'
