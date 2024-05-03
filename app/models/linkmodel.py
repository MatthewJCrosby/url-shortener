from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, BooleanAttribute
from pynamodb.exceptions import UpdateError


class LinkModel(Model):

    """
    This is the pynamo representation of objects in the dynamoDB, ensuring easier operations with the DB
    """


    class Meta:
        table_name = 'URLShortenerTable'
        region = 'us-west-2'

    # UnicodeAttribute is used to store string data in Unicode format
    #hash_key is the primary key for the DB table
    short_url = UnicodeAttribute(hash_key=True)
    #NumberAttribute stores an integer
    clicks = NumberAttribute(default=0)
    original_url = UnicodeAttribute()