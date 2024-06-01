from utils.config import ma
from models import Pet


class PetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'pet_type', 'race', 'color', 'size', 'sex', 'age', 'vaccine',
                  'sterilization', 'health_status', 'description', 'organization', 'image', 'ubication')


pet_schema = PetSchema()
pet_schemas = PetSchema(many=True)
