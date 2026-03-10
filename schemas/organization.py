from utils.config import ma
from marshmallow import fields, validate

class OrgSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=45))
    adress = fields.Str(validate=validate.Length(max=45))
    phone = fields.Int()
    email = fields.Email(required=True, validate=validate.Length(max=45))
    user = fields.Int(required=True)
    logo = fields.Str(validate=validate.Length(max=45))
    role = fields.Int(required=True)

org_schema = OrgSchema()
org_schemas = OrgSchema(many=True)
