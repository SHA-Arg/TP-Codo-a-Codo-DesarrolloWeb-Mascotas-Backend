from flask import Blueprint, request, jsonify
from models import Organization
from utils.config import db
from schemas.organization import org_schema

organization_bp = Blueprint('/organizaciones', __name__)


@organization_bp.get('/organizaciones')
def get_organizations():
    try:
        all_organizations = Organization.query.all()
        org_list = [
            {
                'id': org.id,
                'name': org.name,
                'adress': org.adress,
                'phone': org.phone,
                'email': org.email,
                'user': org.user,
                'logo': org.logo,
                'role': org.role
            }
            for org in all_organizations
        ]
        if not all_organizations:
            return jsonify({'message': 'Todavía no hay organizaciones registradas'}), 404

        return jsonify({'organizations': org_list})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


@organization_bp.get('/organizaciones/<id>')
def get_organization(id):
    try:
        org = Organization.query.get(id)

        if org:
            return jsonify({'organization': org_schema.dump(org)})

        return jsonify({'message': 'Organización no encontrada'}), 404

    except Exception as e:
        return jsonify({'error': str(e)})


@organization_bp.post('/organizaciones')
def create_organization():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON inválido'}), 400

        errors = org_schema.validate(data)
        if errors:
            return jsonify({'error': 'Datos inválidos', 'details': errors}), 400

        new_org = Organization(
            name=data.get('name'),
            adress=data.get('adress'),
            phone=data.get('phone'),
            email=data.get('email'),
            user=data.get('user'),
            logo=data.get('logo'),
            role=data.get('role')
        )
        db.session.add(new_org)
        db.session.commit()
        return jsonify({'organization': org_schema.dump(new_org), 'message': 'Organización registrada exitosamente'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@organization_bp.delete('/organizaciones/<id>')
def delete_organization(id):
    try:
        org = Organization.query.get(id)

        if not org:
            return jsonify({'message': 'Organizacion no encontrada'}), 404

        db.session.delete(org)
        db.session.commit()

        return jsonify({'organization': org_schema.dump(org), 'message': 'Organizacion eliminada exitosamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)})


@organization_bp.put('/organizaciones/<id>')
def update_organization(id):
    try:
        org = Organization.query.get(id)
        if not org:
            return jsonify({'message': 'Organizacion no encontrada'}), 404

        data = request.get_json()
        if not data:
            return jsonify({'error': 'JSON inválido'}), 400

        errors = org_schema.validate(data, partial=True)
        if errors:
            return jsonify({'error': 'Datos inválidos', 'details': errors}), 400

        for key, value in data.items():
            if hasattr(org, key):
                setattr(org, key, value)
        db.session.commit()
        return jsonify({'organization': org_schema.dump(org)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
