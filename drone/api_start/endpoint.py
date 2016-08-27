from drone.api_start import api
from drone.main import db
from drone.models import UserModel

@api.route('/',methods=['GET'])
def start():
    count = db.session.query(UserModel).count()
    return "Count of users from psql "+str(count)
