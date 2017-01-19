from graphene import relay,ObjectType,Schema,String
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
from sqlalchemy.ext.declarative import declarative_base
from drone.models.user import UserModel
from drone.main import db

Base = declarative_base()
Base.query = db.session.query_property()

class Users(SQLAlchemyObjectType):
    """
    creating UserModel for the graphql to query
    """
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)

class Query(ObjectType):
    # users = graphene.List(Users)
    # node = relay.Node.Field()
    user = SQLAlchemyConnectionField(Users,name=String(),email=String()) # add more field which need to be filter
    node = relay.Node.Field(Users) # use to resolve the node field

    def resolve_user(self, args, context, info):
        query = Users.get_query(context)  # SQLAlchemy query
        #filter query TODO : filter query in different way
        if args and 'name' in args:
            return query.filter(UserModel.name == args['name'])
        if args and 'email' in args:
            return query.filter(UserModel.email == args['email'])
        else:
            return query.all()


schema = Schema(query=Query)