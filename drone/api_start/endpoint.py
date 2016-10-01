from drone.api_start import api
from drone.main import db
from drone.models import UserModel
from flask import request,current_app
from drone.utility.nishu import add_user_in_db,get_user_names,set_user_credentials,authenticate_user


@api.route('/',methods=['GET'])
def start():
    count = db.session.query(UserModel).count()
    return "Count of users from psql "+str(count)

@api.route('/users',methods=['GET'])
def users():
    all_users = get_user_names()
    return all_users

@api.route('/users',methods=['POST'])
def insert_user():
    data = request.get_json()

    if not data or 'id' not in data :
        return "Data is not provided ",414

    add_user_in_db(data)
    return "ok",200

@api.route('/new_user',methods=['POST'])
def new_User():
    user = request.get_json()

    if not user or 'username' and 'password' not in user :
        return "Data is not Valid",414

    set_user_credentials(user)
    return "ok",200

@api.route('/login',methods=['POST'])
def login():
    user = request.get_json()

    if not user or 'username' and 'password' not in user :
        return "Invalid Data",412
    name=user['username']
    passwd=user['password']
    authenticate_user(name,passwd)
    return "ok",200