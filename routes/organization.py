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
    id = request.json['id'] 
    name = request.json['name']
    adress = request.json['adress']
    phone = request.json['phone']
    email = request.json['email'] 
    user = request.json['user']
    logo = request.json['logo'] 
    role = request.json['role']

    new_org = Organization(id, name, adress, phone, email, user, logo, role)

    db.session.add(new_org)
    db.session.commit()

    return org_schema.dump(new_org),({})