from flask import Blueprint, request, jsonify
from models import Organization
from utils.config import db
from schemas.organization import org_schema

organization = Blueprint('/organizaciones', __name__)

@organization.get('/organizaciones')
def get_organizations():
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

    return jsonify({'organizations': org_list})
        
@organization.get('/organizaciones/<id>')
def get_organization(id):
    organization = Organization.query.get(id)
    print(organization)
    
    if organization:
        return org_schema.jsonify({organization})
    else:
        return jsonify({'message': 'Organización no encontrada'}), 404 

@organization.post('/organizaciones')
def create_organization():
    name = request.form['name']
    adress = request.form['adress']
    phone = request.form['phone']
    email = request.form['email'] 
    user = request.form['user']
    logo = request.form['logo'] 
    role = request.form['role']

    new_org = Organization(name = name, adress = adress, phone = phone, email = email, user = user, logo = logo, role = role)

    db.session.add(new_org)
    db.session.commit()

    return org_schema.dump(new_org),({'message': 'Organización registrada exitosamente'})