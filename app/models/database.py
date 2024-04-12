from typing import Optional
from boto3.session import Session
from app.service.url_shortener import Link
import os

# this file will contain connection to the database, and database logic


class LinkDatabase:
    def __init__(self, endpoint_url:str, table_name:str):
        # connection parameters
        self.session = Session()
        self.dynamodb = self.session.resource("dynamodb", endpoint_url=endpoint_url)  # Use the configurable endpoint URL
        self.table = self.dynamodb.Table(table_name)

# CREATE
    def create_link(self, link: Link) -> Link:
        pass
        """
        this function will create an entry in the database
        return a Link object so the input information can be returned
        """


    # READ
    def get_link(self, short_url: str) -> Link:
        pass
        """
        this function will take a shortlink as a key, and return the link object as the value
        """


    # UPDATE
    def update_link(self, link: Link) -> Link:
        pass
        """
        This function will take a link object and update the relevant DB entry .
        Returns a Link object so the updated data can be returned. 
        """


    # DELETE
    def delete_link(self, link_id: str) -> bool:
        pass
        """
        this function will  take a shortlink as a key and delete the corresponding entry.
        """
