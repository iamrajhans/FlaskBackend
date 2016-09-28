#include your common config to your app
import logging
SQLALCHEMY_TRACK_MODIFICATIONS = True


SECRET_KEY ='secret key'


DEBUG = True


#------- Database URI ----------#
SQLALCHEMY_DATABASE_URI= 'postgresql://Rajhans:laviraj123@localhost:5432/flaskmovie'


#-------- Sentry ------#


DSN_SENTRY ='https://8bde72b5d31d49b497f1e49226ae0f96:71b0bc035d684846803e5e6ef725ca96@app.getsentry.com/94768'
