from datetime import datetime
from splitway import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.email}')"

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column( db.String(120), nullable=False)
    first_name = db.Column( db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    current_address = db.Column(db.String(250), nullable=False)
    destination_address = db.Column(db.String(250), nullable=False)
    time = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return ({"event_name":self.event_name,"first_name":self.first_name,"email":self.email,"current_address":self.current_address,"destination_address":self.destination_address,"time":self.time})
db.create_all()