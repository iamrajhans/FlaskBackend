from drone.main import db
from datetime import datetime

class AppAuthentication(db.Model):
    __tablename__ = 'app_authentication'

    id       = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(150))
    api_key  = db.Column(db.String(150))
    salt     = db.Column(db.String(150))

    def as_dict(self):
        return {c.name: datetime.strftime(getattr(self, c.name), '%Y-%m-%d %H:%M:%S') if isinstance(getattr(self, c.name),datetime) else getattr(self,c.name)for c in self.__table__.columns}

    def __repr__(self):
        return "<AppAuthentication ('%s')>" % (self.api_key)
