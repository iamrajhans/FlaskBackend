from flask import jsonify
from flask_graphql import GraphQLView
from drone.api_start import api
from drone.main import db
from drone.models import UserModel
from drone.models.schema import schema
from drone.utility.auth_required import auth_decorator
from drone.utility.nishu import get_user_names


@api.route('/',methods=['GET'])
def start():
    """
    Returns: entry endpoint to check connected to db and working correctly
    """
    count = db.session.query(UserModel).count()
    return "Count of users "+str(count),200

@api.route('/users',methods=['GET'])
@auth_decorator
def users():
    """
    Returns: get all users details 
    """
    all_users = get_user_names()
    return jsonify({'result':'success','data':{'users':all_users}}),200

@api.route('/graphql',methods=['GET'])
@auth_decorator
def graphql():
    """
    endpoint to fetch the data
    Returns: query result of graphql
    """
    return GraphQLView(schema=schema,graphiql=True).dispatch_request(),200