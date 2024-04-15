from typing import Optional
from boto3.session import Session
from app.models.link import Link
import os

# this file will contain connection to the database, and database logic


class LinkDatabase:
    def __init__(self, table_name:str):

        # connection parameters
        self.session = Session(
            aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
            region_name='us-west-2'
        )
        self.dynamodb = self.session.resource("dynamodb")
        self.table = self.dynamodb.Table(table_name)
        self.users_table = self.dynamodb.Table('UsersTable')

# CREATE
    def create_link(self, link, user):
        try:
            # Convert the Link object to a dict for DB inseriton in the format shortlink : clicks : original_url
            item = link.dict()

            # place the link into the link DB
            self.table.put_item(Item=item)

            # Update the user's links set in the Users table
            self.update_user_entry(user, link.short_url)
            return True

        # in case an error occurs
        except Exception as e:
            print(f"Failed to create link: {e}")
            return False

    def update_user_entry(self, username, short_url):
        """
        user table keeps a set of each users links for listing / editing / data / clicks retrieval
            for now, it assumes the user exists, later on it will verify a user is in the table before link creation
        """

        #db format username: set(links)
        try:
            self.users_table.update_item(
                Key={'username': username},
                UpdateExpression='ADD links :newLink',
                ExpressionAttributeValues={':newLink': {short_url}},
                ReturnValues="UPDATED_NEW"
            )
        except Exception as e:
            print(f"Failed to update user entry: {e}")



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
