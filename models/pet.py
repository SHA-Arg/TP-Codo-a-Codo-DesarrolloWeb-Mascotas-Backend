from utils import db

class Pet(db.Model):
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.timestamp())

    def __init__(self, name, age, description):
        self.name = name
        self.age = age
        self.description = description

    def __str__(self) -> str:
        return self.name
