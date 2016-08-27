from drone.api_start import api
from drone.main import db
from drone.models import UserModel

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

