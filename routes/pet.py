from schemas.pets import pet_schema, pet_schemas
from models import Pet
from utils.config import db
from flask import Blueprint, request, jsonify, send_from_directory, current_app
from werkzeug.utils import secure_filename
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


pets = Blueprint('/mascotas', __name__)
# current_app.config['PATH_IMG_MASCOTAS'] = '/mascotas/img'


# Obtener listado de mascotas
@pets.get('/mascotas')
def get_pets():
    try:
        all_pets = Pet.query.all()
        pets_list = [
            {
                'id': pet.id,
                'name': pet.name,
                'pet_type': pet.pet_type,
                'race': pet.race,
                'color': pet.color,
                'size': pet.size,
                'age': pet.age,
                'sex': pet.sex,
                'vaccine': pet.vaccine,
                'sterilization': pet.sterilization,
                'health_status': pet.health_status,
                'description': pet.description,
                'organization': pet.organization,
                'image': pet.image,
                'ubication': pet.ubication
            }
            for pet in all_pets
        ]

        if not all_pets:
            return jsonify({'message': 'Todavía no tienes mascotas publicadas'}), 404

        else:
            # print(pet.__dict__)
            return jsonify({'pets': pets_list})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Obtener mascota por id
@pets.get('/mascotas/<id>')
def get_pet(id):

    try:
        pet = Pet.query.get(id)

        if pet:
            return jsonify({'pet': pet_schema.dump(pet)})

        else:
            return jsonify({'message': 'Mascota no encontrada'}), 404

    except Exception as e:
        return jsonify({'error': str(e)})


# Crear nueva mascota
@pets.post('/mascotas')
def create_pets():
    try:
        pets = Pet.query.all()
        pet_list = pet_schemas.dump(pets)

        name = request.form['name']
        pet_type = request.form['pet_type']
        race = request.form['race']
        color = request.form['color']
        size = request.form['size']
        sex = request.form['sex']
        age = request.form['age']
        vaccine = request.form['vaccine']
        sterilization = request.form['sterilization']
        health_status = request.form['health_status']
        description = request.form['description']
        organization = request.form['organization']
        image = request.form['image']
        ubication = request.form['ubication']

        new_pet = Pet(

            name=name,
            pet_type=pet_type,
            race=race,
            color=color,
            size=size,
            sex=sex,
            age=age,
            vaccine=vaccine,
            sterilization=sterilization,
            health_status=health_status,
            description=description,
            organization=organization,
            image=image,
            ubication=ubication
        )

        db.session.add(new_pet)
        db.session.commit()

        if any(pet['name'] == name and pet['description'] == description for pet in pet_list):
            return jsonify({'message': 'Esta mascota ya existe en sus registros'})

        else:
            db.session.add(new_pet)
            db.session.commit()

            return jsonify([pet_schema.dump(new_pet), {'message': 'Mascota creada exitosamente'}])

    except Exception as e:
        return jsonify({'error': str(e)})


# Eliminar mascota por id
@pets.delete('/mascotas/<id>')
def delete_pet(id):
    try:
        pet = Pet.query.get(id)

        if not pet:
            return jsonify({'message': 'Mascota no encontrada'}), 404

        db.session.delete(pet)
        db.session.commit()

        return jsonify({'pet': pet_schema.dump(pet), 'message': 'Mascota eliminada exitosamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)})


@pets.put('/mascotas/<id>')
def update_pet(id):
    try:
        pet = Pet.query.get(id)

        if not pet:
            return jsonify({'message': 'Mascota no encontrada'}), 404

        # Usar request.json directamente en lugar de request.get_json()

        data = request.form

        # Iterar sobre las claves del diccionario y actualizar los atributos correspondientes
        for key, value in data.items():
            setattr(pet, key, value)

        db.session.commit()

        # Devolver la representación JSON actualizada de la mascota
        return jsonify({'pet': pet_schema.dump(pet)})

    except Exception as e:
        # Manejar errores y devolver una respuesta JSON con un código de estado 500
        return jsonify({'error': str(e)}), 500
