from utils.config import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name
    
    organization = db.relationship('Organization', backref = 'role.id', lazy = True)