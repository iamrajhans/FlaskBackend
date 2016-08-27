#include your common config to your app
import logging
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY ='seceret key'

DEBUG = True

#------- Database URI ----------#
SQLALCHEMY_DATABASE_URI= 'postgresql://username:password@localhost:5432/databasename'

#-------- Sentry ------#

DSN_SENTRY ='yoour sentry dsn here'
