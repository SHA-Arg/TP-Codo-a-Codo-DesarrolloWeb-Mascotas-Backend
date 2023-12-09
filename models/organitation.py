from utils.config import db


class organitation(db.Model):

    id = db.Column(db.Integer(11), primary_key=True)
    name = db.Column(db.String(45))
    address = db.Column(db.String(45))
    phone = db.Column(db.Integer(30))
    email = db.Column(db.String(45))
    logo = db.Column(db.String(45))

    def __init__(self, name, adress, phone, email):
        self.name = name
        self.adress = adress
        self.phone = phone
        self.email = email

    def __str__(self) -> str:
        return self.name

    org = db.relationship('Org', backref='organization.id', lazy=True)
