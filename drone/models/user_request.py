from drone.main import db
from datetime import datetime

class UserRequest(db.Model):
    __tablename__ = 'request_referral'
    id = db.Column(db.String(255),autoincrement=True,primary_key=True)
    user_id = db.Column(db.String(100), nullable=True)
    from_user = db.Column(db.String(255),nullable=False)
    to_user = db.Column(db.String(255),nullable=False)
    request_type = db.Column(db.String(255),nullable=False)
    referral_id = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.TIMESTAMP,nullable=True)
    updated_at = db.Column(db.TIMESTAMP,nullable=True)

    def as_dict(self):
        return {c.id: datetime.strftime(getattr(self, c.id), '%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.id),datetime) else getattr(self, c.id) for c in self.__table__.columns}

    def __repr__(self):
        return "<UserRequest ('%s')>" % (self.id)