from drone.api_start import api
from drone.main import db
from drone.models import UserModel
from flask import request,current_app

@api.route('/',methods=['GET'])
def start():
    count = db.session.query(UserModel).count()
    return "Count of users from psql "+str(count)

@api.route('/users',methods=['GET'])
def users():
    totalUsers = []
    users = db.session.query(UserModel).all()

#----- add to list the users -----#
    for user in users :
        totalUsers.append(user.name)

    return str(totalUsers)

@api.route('/users',methods=['POST'])
def insert_user():
    data = request.get_json()

    if not data or 'id' not in data :
        return "Data is not provided ",414
    current_app.logger.info('data : '+str(data))
    add_user = UserModel(
        id    = data['id'],
        name  = data['name'],
        email = data['email']
    )

    db.session.add(add_user)
    db.session.flush()

    return "ok",200
