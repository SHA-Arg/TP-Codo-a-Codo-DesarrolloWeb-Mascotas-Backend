from flask import Blueprint, request, jsonify
from models import Pet
from utils.config import db
from schemas.pets import pet_schema, pet_schemas

pets = Blueprint('/mascotas', __name__)


@pets.route('/mascotas')
def get_pets():
    all_pets = Pet.query.all()
    pets_list = [
        {
            'id': pet.id, 
            'name': pet.name, 
            'pet_type': pet.pet_type, 
            'age': pet.age, 
            'sex': pet.sex, 
            'vaccine': pet.vaccine, 
            'sterilization': pet.sterilization, 
            'health_status': pet.health_status, 
            'description': pet.description, 
            'organization': pet.organization, 
            'image': pet.image
        } 
        for pet in all_pets
    ]
    return jsonify({'pets': pets_list})
   


@pets.route('/mascotas', methods = ['POST'])
def create_mascotas():
    name = request.json['name']
    pet_type = request.json['pet_type']
    sex = request.json['sex']
    age = request.json['age']
    vaccine = request.json['vaccine']
    sterilization = request.json['sterilization']
    health_status = request.json['health_status']
    description = request.json['description']
    organization = request.json['organization']
    image = request.json['image']

    new_pet = Pet(name, pet_type, sex, age, vaccine, sterilization, health_status, description, organization, image)
    
    db.session.add(new_pet)
    db.session.commit()
    
    return jsonify([pet_schema.dump(new_pet), {'message': 'Pet created successfully'}])
    
@pets.route('/mascotas/<id>', methods = ['DELETE'])
def delete_pet(id):
    pet = pet.query.get(id)
    db.session.delete(pet)
    db.session.commit()

    return pet_schema.jsonify(pet)

