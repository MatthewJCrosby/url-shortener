import uuid

from pydantic import BaseModel
from typing import Optional
from app.models.database import LinkDatabase
from app.models.link import Link

"""
This file is a helper that recieves data from api_handlers 
and converts it into the short_link format needed for the databse
"""



#link class defines how the data should look.


def create_shortened_url(original_url: str, short_url: Optional[str], username: str) -> str:

    # open a connection to the DB
    db = LinkDatabase("URLShortenerTable")

    # if no shortlink was provided, create one
    if not short_url:
        short_url = generate_url(db)  # Generate short URL if not provided

    # create a Link object
    link = Link(original_url=str(original_url), short_url=short_url)

    # create an entry in the DB
    if db.create_link(link, username):
        return link.short_url

    # if something went wrong
    else:
        raise Exception("Database insertion failed")

def generate_url(db) -> str:

    #create a 8 digit uuid as shortlink
    url = str(uuid.uuid4())[:8]

    #if it exists, create another until it's unique in the DB
    while db.get_link(url):
        url = str(uuid.uuid4())[:8]

    #return as a string
    return str(url)


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