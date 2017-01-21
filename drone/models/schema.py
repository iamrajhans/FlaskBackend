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
    """
    Query class to run the graphql query
    """
    # users = graphene.List(Users)
    user = SQLAlchemyConnectionField(Users,name=String(),email=String()) # add more field which need to be filter
    node = relay.Node.Field(Users) # use to resolve the node field

    def resolve_user(self, args, context, info):
        """

        Args:
            args: arguments which are pass through the user node
            context: context of the query
        filters : filtering  on the basis of the table column keys and checking that key(column name) in argument
        Returns: if arguments are given and if that node is prsent then it is return

        """
        query = Users.get_query(context)  # SQLAlchemy query
        #filter query TODO : filter query in different way (Done)
        for column_name in UserModel.__table__.columns.keys():
            if column_name in args:
                return query.filter(getattr(UserModel,column_name) == args.get(column_name))


schema = Schema(query=Query)