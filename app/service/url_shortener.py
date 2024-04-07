
from pydantic import BaseModel
from typing import Optional


"""
This file is a helper that recieves data from api_handlers 
and converts it into the short_link format needed for the databse
"""

#link class defines how the data should look.
class Link(BaseModel):
    id: Optional[str]
    original_url: str
    short_url: str

def create_shortened_url(original_url: str) -> str:
    pass
    """ This function will take information from api_handlers, call generate_url, create a link object  
        send the information to database.py for insertion
        returns a boolean to api_handlers upon completion
    """


def generate_url(short_url: str) -> str:
    pass
    """
    This function is a helper function of create_shortened url, and will handle the generation of a link
    and ensuring it doesnt already exist
    """

def update_short_url(short_url: str, new_url: str) -> bool:
    """
    This function will first verify the link exists
    then ask the databse to update the entry, or return False if the link does not exist
    """


def delete_short_url(short_url: str) -> bool:
    """
    This function will first verify the link exists
    then ask the database to delete it.
    """