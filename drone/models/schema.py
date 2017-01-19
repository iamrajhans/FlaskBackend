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
    node = relay.Node.Field()
    user = SQLAlchemyConnectionField(Users,name=String())

    def resolve_users(model,self, args, context, info):
        query = Users.get_query(context)  # SQLAlchemy query
        if args and 'name' in args:
            query = query.filter(getattr(model,'name') == args['name'])
            return query
        else:
            return query


schema = Schema(query=Query)