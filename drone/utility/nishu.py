from drone.main import db
from drone.models import AppAuthentication,UserModel
from os import urandom

def get_application_model(api_key):

    return db.session.query(AppAuthentication).filter_by(api_key=api_key).first()

def add_user_in_db(data):
    add_user = UserModel(
        id=data['id'],
        name=data['name'],
        email=data['email']
    )

    db.session.add(add_user)
    db.session.flush()

def get_user_names():
    totalUsers=[]
    users = db.session.query(UserModel).all()
    # ----- add to list the users -----#
    for user in users:
        totalUsers.append(user.name)
    return totalUsers

def set_user_credentials(user):
    set_user = AppAuthentication()



def generate_key():

    key = urandom(48).encode('hex')
    return key
