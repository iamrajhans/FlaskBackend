from flask import request,jsonify
from drone.api_start import api
from drone.main import db
from drone.models import UserModel
from drone.utility.nishu import add_user_in_db,get_user_names,set_user_credentials,authenticate_user
from drone.utility.auth_required import auth_decorator


@api.route('/',methods=['GET'])
def start():
    count = db.session.query(UserModel).count()
    return "Count of users from psql "+str(count)

@api.route('/users',methods=['GET'])
@auth_decorator
def users():
    all_users = get_user_names()
    return jsonify({'result':'success','data':{'users':all_users}}),200

@api.route('/users',methods=['POST'])
@auth_decorator
def insert_user():
    data = request.get_json()

    if not data or 'id' not in data :
        return "Data is not provided ",414

    add_user_in_db(data)
    return jsonify({'result':'success','message':'user is created successfully'}),200

@api.route('/sign_up',methods=['POST'])
def new_User():
    user = request.get_json()

    if not user or 'username' and 'password' not in user :
        return "Data is not Valid",414

    api_key = set_user_credentials(user)
    return jsonify({'result':'success','data':{'key':api_key}}),200

@api.route('/login',methods=['POST'])
def login():
    user = request.get_json()

    if not user or 'username' and 'password' not in user :
        return "Invalid Data",412
    name=user['username']
    passwd=user['password']
    authenticate_user(name,passwd)
    return "ok",200