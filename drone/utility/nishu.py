from drone.main import db
from drone.models import AppAuthentication


def get_application_model(api_key):

    return db.session.query(AppAuthentication).filter_by(api_key=api_key).first()


