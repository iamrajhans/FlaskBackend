from drone.api_start import api
from drone.main import db
from drone.models import UserModel
from flask import request,current_app
from drone.utility.nishu import add_user_in_db,get_user_names

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
