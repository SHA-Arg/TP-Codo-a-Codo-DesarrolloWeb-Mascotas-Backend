from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from models import organitation
from schemas.pets import pet_schema, pet_schemas


logo_org_folder = 'public/images/logos_org'


def get_orgs():
    all_orgs = Org.query.all()
    orgs_list = [
        {
            'id': org.id,
            'name': org.name,
            'address': org.address,
            'phone': org.phone,
            'email': org.email,
            'logo_image': org.image
        }
        for org in all_orgs
    ]

    return jsonify({'orgs': orgs_list})


def get_org(id):
    org = Org.query.get(id)

    print(org)

    if org:
        print(org.__dict__)
        return jsonify({'org': org_schema.dump(org)})

    else:
        return jsonify({'message': 'Organizacion no encontrada'}), 404


def create_org():
    name = request.json['name']
    address = request.json['address']
    phone = request.json['phone']
    email = request.json['email']
    logo_img = request.json['logo_img']

    image = secure_filename(image.filename)

    name_base, extension = os.path.splitext(name_image)

    name_image = f"org_{id}{extension}"
    image.save(os.path.join(img_folder, name_image))

    new_org = Org(name, address, phone, email, logo_img)

    org_db.session.add(new_org)
    org_db.session.commit()

    return jsonify([org_schema.dump(new_org), {'message': 'Pet created successfully'}])


def delete_org(id):
    org = Org.query.get(id)

    if not org:
        return jsonify({'message': 'Organizacion no encontrada'}), 404

    org_db.session.delete(org)
    org_db.session.commit()

    return org_schema.jsonify(org)


def update_org(id):
    org = get_org(id)
    if org:
        data = request.get_json()
        org.update(data)
        return jsonify({'org': org})
    else:
        return jsonify({'error': 'Organizacion no encontrada'}), 404


def update_org(id):
    org = Org.query.get(id)
    if not org:
        return jsonify({'message': 'Organizacion no encontrada'}), 404
    else:
        org.name = request.json.get('name', org.name)
        org.address = request.json.get('address', org.address)
        org.phone = request.json.get('phone', org.phone)
        org.email = request.json.get('email', org.email)
        org.logo_img = request.json.get('logo_img', org.logo_img)

        db.session.commit()
        return org_schema.jsonify(org)
