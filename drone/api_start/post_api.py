from flask import request,jsonify
from drone.api_start import api
from drone.utility.auth_required import auth_decorator
from drone.utility.nishu import add_user_in_db,set_user_credentials,authenticate_user


@api.route('/users',methods=['POST'])
@auth_decorator
def insert_user():
    data = request.get_json()

    if 'id' not in data :
        return jsonify({'result':'error','message':'Data is not provided' }),414

    add_user_in_db(data)
    return jsonify({'result':'success','message':'user is created successfully'}),200

@api.route('/sign_up',methods=['POST'])
def new_User():
    user = request.get_json()

    if 'username' and 'password' not in user :
        return jsonify({'result':'error','message':'missing data'}),414

    api_key = set_user_credentials(user)
    return jsonify({'result':'success','data':{'key':api_key}}),200

@api.route('/login',methods=['POST'])
def login():
    user = request.get_json()

    if 'username' and 'password' not in user :
        return jsonify({'result': 'error', 'message': 'missing data'}), 414
    name=user['username']
    passwd=user['password']
    authenticate_user(name,passwd)
    return jsonify({'result': 'success', 'message': 'login successful'}),200