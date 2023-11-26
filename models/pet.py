from utils.config import db

class Pet(db.Model):
       
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(45))
    pet_type = db.Column(db.Integer , db.ForeignKey('pet_type.id'))
    sex = db.Column(db.String(10))
    age = db.Column(db.Integer)
    vaccine = db.Column(db.String(10))
    sterilization = db.Column(db.String(10))
    health_status = db.Column(db.String(45))
    description = db.Column(db.String(250))
    organization = db.Column(db.Integer, db.ForeignKey('organization.id'))
    image = db.Column(db.String(45))

    def __init__(self, name, pet_type, sex, age, vaccine, sterilization, health_status, description, organization, image):
        self.name = name
        self.pet_type = pet_type
        self.sex = sex
        self.age = age
        self.vaccine = vaccine
        self.sterilization = sterilization
        self.health_status = health_status
        self.description = description
        self.organization = organization
        self.image = image

    def __str__(self) -> str:
        return self.name
    
    
    
    
