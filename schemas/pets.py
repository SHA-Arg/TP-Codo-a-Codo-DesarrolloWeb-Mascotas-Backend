from utils.config import ma
from models import Pet

class PetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'pety_type', 'sex','age', 'vaccine', 'sterilization', 'health_status', 'description', 'organization', 'image')

pet_schema = PetSchema()
pet_schemas = PetSchema(many = True)