from app import db
from sqlalchemy_utils.types.choice import ChoiceType


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)


class DataCenter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    address = db.Column(db.String(255))
    bind_width = db.Column(db.String(255))
    link_name = db.Column(db.String(255))
    contact_phone = db.Column(db.String(255))
    create_time = db.Column(db.DateTime())
    update_time = db.Column(db.DateTime())
    remark = db.Column(db.String(255))

    def _to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "bind_width": self.bind_width,
        }

        # def update(self, **kwargs):
        #     for key, value in kwargs.items():
        #         setattr(self, key, value)
