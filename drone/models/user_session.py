from drone.main import db
from datetime import datetime

class UserSession(db.Model):
    __tablename__ = 'user_session'
    id = db.Column(db.String(255),autoincrement=True,primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    session_start = db.Column(db.TIMESTAMP,nullable=False)
    session_end = db.Column(db.TIMESTAMP,nullable=False)
    isValid = db.Column(db.Boolean,nullable=False)
    user_plan = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.TIMESTAMP,nullable=False)
    updated_at = db.Column(db.TIMESTAMP,nullable=False)

    def as_dict(self):
        return {c.id: datetime.strftime(getattr(self, c.id), '%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.id),datetime) else getattr(self, c.id) for c in self.__table__.columns}

    def __repr__(self):
        return "<UserSession ('%s')>" % (self.id)