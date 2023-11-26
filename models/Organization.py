from utils.config import db

class Organization(db.Model):
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(45))
    adress = db.Column(db.String(45))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(45))
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    logo = db.Column(db.String(45))
    role = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __init__ (self, name, adress, phone, email):
        self.name = name
        self.adress = adress
        self.phone = phone 
        self.email = email

    def __str__(self) -> str:
            return self.name
    
    pet = db.relationship('Pet', backref = 'organization.id', lazy = True)
    

