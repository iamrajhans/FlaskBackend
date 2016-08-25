from drone.main import db
from datetime import datetime

class UserModel(db.model):
    __tablename__ = 'user'
    id    = db.Column(db.Integer,primary_key=True)
    name  = db.Column(db.String(100),nullable=True)
    email = db.Column(db.String(150),nullable=True)


def as_dict(self):
    return {c.name: datetime.strftime(getattr(self, c.name), '%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name),datetime) else getattr(self, c.name) for c in self.__table__.columns}

def __repr__(self):
        return "<User ('%s')>" % (self.id)

