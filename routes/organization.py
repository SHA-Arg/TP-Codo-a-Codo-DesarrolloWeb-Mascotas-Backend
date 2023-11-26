from flask import Blueprint, request, jsonify
from models import Organization
from utils.config import db

organization = Blueprint('/organizaciones', __name__)

@organization.route('/organizaciones')
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
        

    return jsonify('listado organizaciones')
