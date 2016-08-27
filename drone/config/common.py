#include your common config to your app
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY ='seceret key'

#------- Database URI ----------#
SQLALCHEMY_DATABASE_URI= 'postgresql://username:password@localhost:5432/databasename'

#-------- Sentry ------#

SENTRY_DSN ='add your dsn sentry here'
