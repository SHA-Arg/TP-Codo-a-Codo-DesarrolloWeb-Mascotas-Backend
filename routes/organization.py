from flask import Blueprint, request, jsonify
from models import Organization
from utils.config import db
from schemas.organization import org_schema

organization = Blueprint('/organizaciones', __name__)

@organization.get('/organizaciones')
def get_organizations():
    try:
        all_organizations = Organization.query.all()
        org_list = [
            {       
                'id' : organization.id,
                'name' : organization.name,
                'adress' : organization.adress,
                'phone' : organization.phone,
                'email' : organization.email,
                'user' : organization.user,
                'logo' : organization.logo,
                'role' : organization.role
            }

            for organization in all_organizations
        ]
        if not all_organizations:
            return jsonify({'message': 'Todavía no hay organizaciones registradas'}), 404
                    

        else:
            return jsonify({'organizations': org_list}) 
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
        


@organization.get('/organizaciones/<id>')
def get_organization(id):
    try:

        organization = Organization.query.get(id)
        
        if organization:
            return jsonify({'organization': org_schema.dump(organization)})

        else:
            return jsonify({'message': 'Organización no encontrada'}), 404 
    
    except Exception as e:
        return jsonify({'error': str(e)})



@organization.post('/organizaciones')
def create_organization():
    try:
        name = request.form['name']
        adress = request.form['adress']
        phone = request.form['phone']
        email = request.form['email'] 
        user = request.form['user']
        logo = request.form['logo'] 
        role = request.form['role']

        new_org = Organization(
            name = name, 
            adress = adress, 
            phone = phone, 
            email = email, 
            user = user, 
            logo = logo, 
            role = role
        )

        db.session.add(new_org)
        db.session.commit()

        return org_schema.dump(new_org),({'message': 'Organización registrada exitosamente'})
    
    except Exception as e:
        return jsonify({'error': str(e)})



# Eliminar organización por id
@organization.delete('/organizaciones/<id>')
def delete_organization(id):

    try:
        organization = Organization.query.get(id)

        if not organization:
            return jsonify({'message': 'Organizacion no encontrada'}), 404
        
        db.session.delete(organization)
        db.session.commit()

        return jsonify({'organization': org_schema.dump(organization), 'message': 'Organizacion eliminada exitosamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)})


# versión no probada de UPDATE:

@organization.put('/organizaciones/<id>')
def update_organization(id):

    #folder_img = current_app.config.get('FOLDER_IMG_PETS', 'public/images/pets')
    try:
        organization = Organization.query.get(id)

        if not organization:
            return jsonify({'message': 'Organizacion no encontrada'}), 404

        # Usar request.json directamente en lugar de request.get_json()

        data = request.form # request.son en este entorno?

        # Iterar sobre las claves del diccionario y actualizar los atributos correspondientes
        for key, value in data.items():
            setattr(organization, key, value)
        
        db.session.commit()

        # Devolver la representación JSON actualizada de la mascota
        return jsonify({'organization': org_schema.dump(organization)})

    except Exception as e:
        # Manejar errores y devolver una respuesta JSON con un código de estado 500
        return jsonify({'error': str(e)}), 500