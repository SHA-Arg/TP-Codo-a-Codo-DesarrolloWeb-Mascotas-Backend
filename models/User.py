from utils.config import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45))
    password = db.Column(db.String(50))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    organizations = db.relationship(
        'Organization', backref='user', lazy=True)
