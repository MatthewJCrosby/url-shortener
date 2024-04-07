from typing import Optional
from boto3.session import Session
from app.service.url_shortener import Link
import os

#this file will contain connection to the database, and database logic


LINKS_TABLE_NAME = "LinkShortener"
DYNAMODB_ENDPOINT_URL = os.getenv("DYNAMODB_ENDPOINT_URL", "http://localhost:8000")

#connection parameters
session = Session()
dynamodb = session.resource("dynamodb", endpoint_url=DYNAMODB_ENDPOINT_URL) # Use the configurable endpoint URL
table = dynamodb.Table(LINKS_TABLE_NAME)



#CREATE
def create_link(link: Link) -> None:

    pass
    """
    this function will create an entry in the database
    return a boolean to indicate success or fail
    """

#READ
def get_link(short_url: str) -> Optional[dict]:
    pass
    """
    this function will take a shortlink as a key, and return the link object as the value
    """

#UPDATE
def update_link(link_id: str, data: dict) -> None:
    pass
    """
    This function will take a link object and update the relevant DB entry .
    
    """

#DELETE
def delete_link(link_id: str) -> None:
    pass
    """
    this function will  take a shortlink as a key and delete the corresponding entry.
    """
