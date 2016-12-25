from drone.main import db
from datetime import datetime

class UserRequest(db.Model):
    __tablename__ = 'referral'
    id = db.Column(db.String(255),autoincrement=True)
    from_user = db.Column(db.String(255))
    request_type = db.Column(db.String(255))

    def as_dict(self):
        return {c.id: datetime.strftime(getattr(self, c.id), '%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.id),datetime) else getattr(self, c.id) for c in self.__table__.columns}

    def __repr__(self):
        return "<UserRequest ('%s')>" % (self.id)