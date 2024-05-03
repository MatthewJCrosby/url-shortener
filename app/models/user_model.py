from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, UnicodeSetAttribute

class UserModel(Model):
    class Meta:
        table_name = 'UsersTable'
        region = 'us-west-2'

    # UnicodeAttribute is used to store string data in Unicode format
    username = UnicodeAttribute(hash_key=True)
    links = UnicodeSetAttribute(null=True)
