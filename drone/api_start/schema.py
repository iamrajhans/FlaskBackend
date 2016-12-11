import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from drone.models.user import UserModel

class Users(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(Users)

    def resolve_users(self, args, context, info):
        query = Users.get_query(context)  # SQLAlchemy query
        return query.all()

schema = graphene.Schema(query=Query)