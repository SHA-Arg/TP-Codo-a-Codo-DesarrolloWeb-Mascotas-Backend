from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from utils.config import db
from models import Pet
from schemas.pets import pet_schema, pet_schemas


img_folder = 'public/images/pets'


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


def get_pet(id):
    pet = Pet.query.get(id)
    print(pet)

    if pet:
        print(pet.__dict__)
        return jsonify({'pet': pet_schema.dump(pet)})
    else:
        return jsonify({'message': 'Mascota no encontrada'}), 404


def create_pet():
    name = request.json['name']
    pet_type = request.json['pet_type']
    sex = request.json['sex']
    age = request.json['age']
    vaccine = request.json['vaccine']
    sterilization = request.json['sterilization']
    health_status = request.json['health_status']
    description = request.json['description']
    organization = request.json['organization']
    image = request.files['image']
    image = secure_filename(image.filename)
    name_image = f"pet_{id}{extension}"
    image.save(os.path.join(img_folder, name_image))

    new_pet = Pet(name, pet_type, sex, age, vaccine, sterilization,
                  health_status, description, organization, image)

    db.session.add(new_pet)
    db.session.commit()

    return jsonify([pet_schema.dump(new_pet), {'message': 'Pet created successfully'}])


def delete_pet(id):
    pet = Pet.query.get(id)

    if not pet:
        return jsonify({'message': 'Mascota no encontrada'}), 404

    db.session.delete(pet)
    db.session.commit()

    return pet_schema.jsonify(pet)
    return pet_schema.jsonify(pet)


def update_pet(id):
    pet = get_pet(id)
    if pet:
        data = request.get_json()
        pet.update(data)
        return jsonify({'pet': pet})
    else:
        return jsonify({'error': 'Mascota no encontrada'}), 404
