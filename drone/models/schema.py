from graphene import relay,ObjectType,Schema
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
from drone.models.user import UserModel
from sqlalchemy.ext.declarative import declarative_base
from drone.main import db

Base = declarative_base()
Base.query = db.session.query_property()

class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node,)

class Query(ObjectType):
    # users = graphene.List(Users)
    node = relay.Node.Field()
    user = SQLAlchemyConnectionField(Users)

    def resolve_users(self, args, context, info):
        query = Users.get_query(context)  # SQLAlchemy query
        return query.all()

schema = Schema(query=Query)