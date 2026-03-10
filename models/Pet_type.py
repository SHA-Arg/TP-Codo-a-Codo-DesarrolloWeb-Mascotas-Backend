from utils.config import db


class Pet_type(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    pets = db.relationship('Pet', backref='pet_type', lazy=True)
