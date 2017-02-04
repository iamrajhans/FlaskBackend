from drone.main import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'users'
    id    = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.String(100),nullable=False)
    name  = db.Column(db.String(100),nullable=False)
    last_name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(150),nullable=False)
    birth_date = db.Column(db.TIMESTAMP,nullable=True)
    address = db.Column(db.String(255),nullable=True)
    created_at = db.Column(db.TIMESTAMP , nullable=False)
    updated_at = db.Column(db.TIMESTAMP,nullable=False)
    def as_dict(self):
        return {c.name: datetime.strftime(getattr(self, c.name), '%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name),datetime) else getattr(self, c.name) for c in self.__table__.columns}

    def __repr__(self):
        return "<Users ('%s')>" % (self.name)

