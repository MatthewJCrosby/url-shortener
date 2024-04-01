from typing import Optional
from boto3.dynamodb.conditions import Key
from boto3.session import Session
from pydantic import BaseModel


#this file will contain connection to the database, and database logic


TABLE_NAME = "LinkShortener"

#connection parameters
session = Session()
dynamodb = session.resource("dynamodb", endpoint_url="http://localhost:8000") #local for now
table = dynamodb.Table(TABLE_NAME)

#link class defines how the data should look.
class Link(BaseModel):
    id: Optional[str]
    original_url: str
    short_url: str


def create_link(link: Link) -> None:
    pass
    """
    this function will take data from api_handlers and create an entry in the database
    return a bollean to indicate success or fail
    """


def get_link_by_short_url(short_url: str) -> Optional[dict]:
    pass
    """
    this function will take a shortlink from api_handlers, 
    and return the original URL back to api_handlers
    """

def get_link_by_id(link_id: str) -> Optional[dict]:
    pass
    """
    this function will take a link id from api_handlers, and return the original url to api_handlers
    """

def delete_link(link_id: str) -> None:
    pass
    """
    this function will take a linkID from api_handlers and delete the shortlink from the DB, 
    return a boolean to API handlers to indicate success or fail
    """

def update_link(link_id: str, data: dict) -> None:
    pass
    """
    This function will take information from api_handlers and update the record on the DB
    return a boolean to api handlers
    """
