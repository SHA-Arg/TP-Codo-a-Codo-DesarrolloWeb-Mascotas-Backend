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
                'pet_type': pet.pet_type_id,
                'race': pet.race,
                'color': pet.color,
                'size': pet.size,
                'age': pet.age,
                'sex': pet.sex,
                'vaccine': pet.vaccine,
                'sterilization': pet.sterilization,
                'health_status': pet.health_status,
                'description': pet.description,
                'organization': pet.organization_id,
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
        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON inválido'}), 400

        # Validar con Marshmallow
        errors = pet_schema.validate(data)
        if errors:
            return jsonify({'error': 'Datos inválidos', 'details': errors}), 400

        # Validar duplicados antes de insertar
        existing = Pet.query.filter_by(name=data.get('name'), description=data.get('description')).first()
        if existing:
            return jsonify({'message': 'Esta mascota ya existe en sus registros'}), 409

        new_pet = Pet(
            name=data.get('name'),
            pet_type_id=data.get('pet_type'),
            race=data.get('race'),
            color=data.get('color'),
            size=data.get('size'),
            sex=data.get('sex'),
            age=data.get('age'),
            vaccine=data.get('vaccine'),
            sterilization=data.get('sterilization'),
            health_status=data.get('health_status'),
            description=data.get('description'),
            organization_id=data.get('organization'),
            image=data.get('image'),
            ubication=data.get('ubication')
        )
        db.session.add(new_pet)
        db.session.commit()
        return jsonify({'pet': pet_schema.dump(new_pet), 'message': 'Mascota creada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


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

        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON inválido'}), 400

        errors = pet_schema.validate(data, partial=True)
        if errors:
            return jsonify({'error': 'Datos inválidos', 'details': errors}), 400

        for key, value in data.items():
            fk_map = {'pet_type': 'pet_type_id', 'organization': 'organization_id'}
            actual_key = fk_map.get(key, key)
            if hasattr(pet, actual_key):
                setattr(pet, actual_key, value)
        db.session.commit()
        return jsonify({'pet': pet_schema.dump(pet)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
