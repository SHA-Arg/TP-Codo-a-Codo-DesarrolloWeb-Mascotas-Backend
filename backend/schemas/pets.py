from utils.config import ma
from marshmallow import fields, validate

class PetSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=45))
    pet_type = fields.Int(required=True, attribute='pet_type_id')
    race = fields.Str(validate=validate.Length(max=45))
    color = fields.Str(validate=validate.Length(max=45))
    size = fields.Str(validate=validate.Length(max=45))
    sex = fields.Str(required=True, validate=validate.OneOf(["M", "F"]))
    age = fields.Int(required=True)
    vaccine = fields.Bool()
    sterilization = fields.Bool()
    health_status = fields.Str(validate=validate.Length(max=45))
    description = fields.Str(validate=validate.Length(max=250))
    organization = fields.Int(required=True, attribute='organization_id')
    image = fields.Str(validate=validate.Length(max=145))
    ubication = fields.Str(validate=validate.Length(max=70))

pet_schema = PetSchema()
pet_schemas = PetSchema(many=True)
