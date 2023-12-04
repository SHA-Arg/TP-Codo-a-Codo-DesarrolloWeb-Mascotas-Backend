# from flask import Blueprint, request, jsonify, send_from_directory, current_app
# from werkzeug.utils import secure_filename
# import os
# from utils.config import db
# from models import Pet
# from schemas.pets import pet_schema, pet_schemas
# #from controllers.pet import *



# pets = Blueprint('/mascotas', __name__)



# # Obtener listado de mascotas
# @pets.get('/mascotas')
# def get_pets():
#     all_pets = Pet.query.all()
#     pets_list = [
#         {
#             'id': pet.id, 
#             'name': pet.name, 
#             'pet_type': pet.pet_type, 
#             'race': pet.race, 
#             'color': pet.color, 
#             'size': pet.size, 
#             'age': pet.age, 
#             'sex': pet.sex, 
#             'vaccine': pet.vaccine, 
#             'sterilization': pet.sterilization, 
#             'health_status': pet.health_status, 
#             'description': pet.description, 
#             'organization': pet.organization, 
#             'image': pet.image
#         } 
#         for pet in all_pets 
#     ]

#     return jsonify({'pets': pets_list})
   
# # Obtener mascota por id
# @pets.get('/mascotas/<id>')
# def get_pet(id):
#     pet = Pet.query.get(id)
    
#     print(pet)
   
#     if pet:
#         print(pet.__dict__)
#         return jsonify({'pet': pet_schema.dump(pet)})

#     else:
#         return jsonify({'message': 'Mascota no encontrada'}), 404 
    
# #Obtener mascotas por pet_type
# # def get_pets_by_type(pet_type):
# #     pets_of_type = Pet.query.filter_by(pet_type=pet_type).all()

# #     if pets_of_type:
# #         pets_data = pet_schemas.dump(pets_of_type, many=True)
# #         return jsonify({'pets': pets_data})
# #     else:
# #         return jsonify({'message': 'No se encontraron mascotas de ese tipo'}), 404 

# # Crear nueva mascota
# @pets.post('/mascotas')
# def create_pets():
#     folder_img = current_app.config.get('FOLDER_IMG_PETS', 'public/images/pets')
#     name = request.form['name']
#     pet_type = request.form['pet_type']
#     race = request.form['race']
#     color = request.form['color']
#     size = request.form['size']
#     sex = request.form['sex']
#     age = request.form['age']
#     vaccine = request.form['vaccine']
#     sterilization = request.form['sterilization']
#     health_status = request.form['health_status']
#     description = request.form['description']
#     organization = request.form['organization']
#     image = request.files['image']


#     # Toma el nombre del archivo original como entrada y devuelve un nombre de archivo seguro para su almacenamiento.
#     image_add = secure_filename(image.filename)

#     # Separa el nombre del archivo de su extensión, considerando el punto como separador.
#     name_base, extension = os.path.splitext(image_add)
      

#     new_pet = Pet(
        
#             name = name, 
#             pet_type= pet_type, 
#             race = race, 
#             color = color, 
#             size = size, 
#             sex = sex, 
#             age = age, 
#             vaccine = vaccine, 
#             sterilization = sterilization, 
#             health_status = health_status, 
#             description = description, 
#             organization = organization, 
#             image = f"/{folder_img }/{name_base}"
        
#     )
    
#     db.session.add(new_pet)
#     db.session.commit()
    
    
#      # Obtiene el ID de la nueva mascota después de guardarla en la base de datos
#     new_pet_id = new_pet.id

#     # Construye el nombre de la imagen con el ID
#     name_image = f"pet_{new_pet_id}{extension}"

#     # Actualiza la ruta de la imagen con el nombre final
#     new_pet.image = f"/{folder_img}/{name_image}"

#     # Guarda la nueva mascota con la ruta de la imagen actualizada
#     db.session.commit()

#     # Guarda la imagen
#     image.save(os.path.join(folder_img, name_image))

#     return jsonify([pet_schema.dump(new_pet), {'message': 'Mascota creada exitosamente'}])
    
# # Eliminar mascota por id
# @pets.delete('/mascotas/<id>')
# def delete_pet(id):
#     pet = Pet.query.get(id)

#     if not pet:
#         return jsonify({'message': 'Mascota no encontrada'}), 404
    
#     db.session.delete(pet)
#     db.session.commit()

#     return jsonify({'pet': pet_schema.dump(pet), 'message': 'Mascota eliminada exitosamente'}), 200

# # Modificar mascota
# @pets.put('/mascotas/<id>')
# def update_pet(id):
#     folder_img = current_app.config.get('FOLDER_IMG_PETS', 'public/images/pets')
#     try:
#         pet = Pet.query.get(id)

#         if not pet:
#             return jsonify({'message': 'Mascota no encontrada'}), 404

#         # Usar request.json directamente en lugar de request.get_json()

#         data = {
#             'name': request.form['name'],
#             'pet_type': request.form['pet_type'],
#             'race': request.form['race'],
#             'color': request.form['color'],
#             'size': request.form['size'],
#             'sex': request.form['sex'],
#             'age': request.form['age'],
#             'vaccine': request.form['vaccine'],
#             'sterilization': request.form['sterilization'],
#             'health_status': request.form['health_status'],
#             'description': request.form['description'],
#             'organization': request.form['organization'],
#             'image': request.files['image']
#         }

#         # Iterar sobre las claves del diccionario y actualizar los atributos correspondientes
#         for key, value in data.items():
#             setattr(pet, key, value)

#         # Toma el nombre del archivo original como entrada y devuelve un nombre de archivo seguro para su almacenamiento.
#         #image_add = secure_filename(image.filename)

#         # Separa el nombre del archivo de su extensión, considerando el punto como separador.
#         #name_base, extension = os.path.splitext(image_add)

#         # Construye el nombre de la imagen con el ID
#         #name_image = f"pet_{data.image}{extension}"

#         # Actualiza la ruta de la imagen con el nombre final
#         # new_image = f"/{folder_img}/{name_image}"

#         # data.image = new_image

#         # data.image.save(os.path.join(folder_img, name_image))

#         db.session.commit()

#         # Devolver la representación JSON actualizada de la mascota
#         return jsonify({'pet': pet_schema.dump(pet)})

#     except Exception as e:
#         # Manejar errores y devolver una respuesta JSON con un código de estado 500
#         return jsonify({'error': str(e)}), 500

from flask import Blueprint, request, jsonify, send_from_directory, current_app
from werkzeug.utils import secure_filename
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.config import db
from models import Pet
from schemas.pets import pet_schema, pet_schemas



pets = Blueprint('/mascotas', __name__)
#current_app.config['PATH_IMG_MASCOTAS'] = '/mascotas/img'


# Obtener listado de mascotas
@pets.get('/mascotas')
def get_pets():
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
            'image': pet.image
        }
        for pet in all_pets
    ]

    return jsonify({'pets': pets_list})

# Obtener mascota por id
@pets.get('/mascotas/<id>')
def get_pet(id):
    pet = Pet.query.get(id)

    if pet:
        return jsonify({'pet': pet_schema.dump(pet)})

    else:
        return jsonify({'message': 'Mascota no encontrada'}), 404

#Obtener imagen de mascota por id
# @pets.get(f"/{current_app.config['PATH_IMG_MASCOTAS']}/<filename>")
# def get_image_id(filename):
#     return send_from_directory(current_app.config['PATH_IMG_MASCOTAS'], filename)

# Crear nueva mascota
@pets.post('/mascotas')
def create_pets():
    folder_img = current_app.config.get('FOLDER_IMG_PETS', 'home/andreajota/mysite/public/images/pets')

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
    image = request.files['image']

    # Toma el nombre del archivo original como entrada y devuelve un nombre de archivo seguro para su almacenamiento.
    image_add = secure_filename(image.filename)

    # Separa el nombre del archivo de su extensión, considerando el punto como separador.
    name_base, extension = os.path.splitext(image_add)

    new_pet = Pet(

        name = name,
        pet_type= pet_type,
        race = race,
        color = color,
        size = size,
        sex = sex,
        age = age,
        vaccine = vaccine,
        sterilization = sterilization,
        health_status = health_status,
        description = description,
        organization = organization,
        image = f"/{folder_img }/{name_base}"

    )

    existing_pet = Pet.query.filter(Pet.name == 'name', Pet.description == 'description')


    db.session.add(new_pet)
    db.session.commit()

     # Obtiene el ID de la nueva mascota después de guardarla en la base de datos
    new_pet_id = new_pet.id

    # Construye el nombre de la imagen con el ID
    name_image = f"pet_{new_pet_id}{extension}"

   # Actualiza la ruta de la imagen con el nombre final
    new_pet.image = f"/{folder_img}/{name_image}"

    # Guarda la nueva mascota con la ruta de la imagen actualizada
    db.session.commit()

    # Guarda la imagen
    image.save(os.path.join(folder_img, name_image))
    print(image)


    return jsonify([pet_schema.dump(new_pet), {'message': 'Mascota creada exitosamente'}])

# Eliminar mascota por id
@pets.delete('/mascotas/<id>')
def delete_pet(id):
    pet = Pet.query.get(id)

    db.session.delete(pet)
    db.session.commit()

    return jsonify({'pet': pet_schema.dump(pet), 'message': 'Mascota eliminada exitosamente'}), 200

# Modificar mascota
@pets.put('/mascotas/<id>')
def update_pet(id):
    folder_img = current_app.config.get('FOLDER_IMG_PETS', 'public/images/pets')
    try:
        pet = Pet.query.get(id)

        if not pet:
            return jsonify({'message': 'Mascota no encontrada'}), 404

        # Usar request.json directamente en lugar de request.get_json()

        data = request.form

        # Iterar sobre las claves del diccionario y actualizar los atributos correspondientes
        for key, value in data.items():
            setattr(pet, key, value)



        # Toma el nombre del archivo original como entrada y devuelve un nombre de archivo seguro para su almacenamiento.
        #image_add = secure_filename(data.image.filename)

        # Separa el nombre del archivo de su extensión, considerando el punto como separador.
        #name_base, extension = os.path.splitext(image_add)

        # Construye el nombre de la imagen con el ID
        #name_image = f"pet_{image}{extension}"

        # Actualiza la ruta de la imagen con el nombre final
        #data.image = f"/{folder_img}/{name_image}"

        #data.image = name_image

        #data.image.save(os.path.join(folder_img, name_image))

        db.session.commit()

        # Devolver la representación JSON actualizada de la mascota
        return jsonify({'pet': pet_schema.dump(pet)})

    except Exception as e:
        # Manejar errores y devolver una respuesta JSON con un código de estado 500
        return jsonify({'error': str(e)}), 500