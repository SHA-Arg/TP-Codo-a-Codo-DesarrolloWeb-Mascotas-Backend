from flask import Blueprint

from models import Pet
from utils import response

pets = Blueprint('pets', __name__, url_prefix='/pets')

@pets.route("/", methods=["GET"])
def get_pets():
    pets = Pet.query.all()
    return response({
        "mensaje": "Listado de mascotas",
    })
