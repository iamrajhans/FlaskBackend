from flask import request,jsonify
from drone.api_start import api
from drone.main import db
from drone.models import UserModel
from drone.utility.nishu import get_user_names
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
