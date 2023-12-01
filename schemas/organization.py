from utils.config import ma
from models import Organization

class OrgSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'adress', 'phone','email', 'user', 'logo','role')

org_schema = OrgSchema()
org_schemas = OrgSchema(many = True)