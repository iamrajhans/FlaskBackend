from drone.main import db
from drone.models import AppAuthentication,UserModel
from os import urandom
import bcrypt
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
    username = user['username']
    entry = get_user_entry(username)
    if not entry :
        salt = bcrypt.gensalt()
        passwd = gen_hash(user['password'], salt)
        app_key = generate_key()
        set_user = AppAuthentication(
            username=username,
            password=passwd,
            api_key=app_key,
            salt=salt
        )
        #----- send api key to user for adding custom protocol -----#
        db.session.add(set_user)
        db.session.flush()



def generate_key():
    key = urandom(24).encode('hex')
    return key

def get_user_entry(username):
    return db.session.query(AppAuthentication).filter_by(username=username).first()

def gen_hash(password,salt):
    return bcrypt.hashpw(password,salt)

def authenticate_user(username,password):
    entry = get_user_entry(username)
    if entry :
        server_hash = entry.password
        if bcrypt.checkpw(password,server_hash):
            return "Login successful",200
        else:
            return "Login Credential didn't match",412
    else:
        return "User Entry not found",412