from typing import Optional
from boto3.session import Session
from app.models.link import Link
import os
from pynamodb.exceptions import UpdateError
from app.models.linkmodel import LinkModel
from app.models.user_model import UserModel

# this file will contain connection to the database, and database logic


#convert from Link to LinkModel
def link_to_linkmodel(link:Link) -> LinkModel:
    try:
        link_model = LinkModel(
            short_url=link.short_url,
            clicks=link.clicks,
            original_url=link.original_url
        )
        return link_model
    except Exception as e:
        raise Exception(f"Failed to convert Link to LinkModel: {e}")


#convert from LinkModel to Link
def linkmodel_to_link(linkmodel:LinkModel):
    try:
        link_model = Link(short_url=linkmodel.short_url, clicks=linkmodel.clicks, original_url=linkmodel.original_url)
        return link_model
    except Exception as e:
        raise Exception(f"Failed to convert Link to LinkModel: {e}")



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
    def create_link(self, link:Link, user):
        try:
            # Create a new LinkModel instance with data from the Link object
            link_model = link_to_linkmodel(link)

            # Save the link to the DynamoDB table
            link_model.save()

            # Update the user's links set in the Users table
            self.update_user_entry(user, link.short_url)
            return True

        # in case an error occurs
        except Exception as e:
            raise Exception(f"Failed to create link due to {e}")

    def update_user_entry(self, username, short_url):
        """
        user table keeps a set of each users links for listing / editing / data / clicks retrieval
            for now, it assumes the user exists, later on it will verify a user is in the table before link creation
        """

        #db format username: set(links)
        try:
            user = UserModel.get(username)
            user.links.add(short_url)
            user.save()
        except Exception as e:
            raise Exception(f"Failed to update user due to {e}")



    # READ


    def check_if_key_exists(self, key_value, is_user=False) -> bool:
        #this function will determine if a url or a user already exists.

        table = self.users_table if is_user else self.table
        key_name = 'username' if is_user else 'short_url'
        try:
            return 'Item' in table.get_item(Key={key_name: key_value})
        except Exception as e:
            raise Exception(f"Failed to check for key due to {e}")


    # READ

    def get_link(self, short_url: str) -> Link:
        """
        this function will take a shortlink as a key, and return the link
        """
        try:
            # Attempt to retrieve the link from the DynamoDB table
            link = LinkModel.get(short_url)
            # If the link is found, create a Link object to pass as a response
            res = linkmodel_to_link(link)
            if link:
                return res

        except Exception as e:
            raise Exception(f"Failed to retrieve link {e}")




    def increment_click(self, short_url)-> bool:

        #Increment the click counter for a given short URL, the link should be verified to exist already.

        try:
            link = LinkModel.get(short_url)
            link.clicks += 1
            link.save()
            return True
        except Exception as e:
            raise Exception(f"Failed to update link clicks {e}")

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
