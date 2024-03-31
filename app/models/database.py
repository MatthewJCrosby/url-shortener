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
    #this function will create an entry in the database in the correct format


def get_link_by_short_url(short_url: str) -> Optional[dict]:
    pass
    #this function will grab the original link, when a short_url is passed in

def get_link_by_id(link_id: str) -> Optional[dict]:
    pass
    #this function will gran the original link when the unique id is passed in

def delete_link(link_id: str) -> None:
    pass
    #this function will delete the shortlink from the DB
