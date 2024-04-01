from app.models.database import create_link, get_link_by_short_url


"""
This file is a helper that recieves data from api_handlers 
and converts it into the short_link format needed for the databse
"""
def create_shortened_url(original_url: str) -> str:
    pass
    """ This function will take information from api_handlers, call shorten() to create the shortlink, 
        send the information back to api_handlers
    """


def shorten(short_url: str) -> str:
    pass
    """
    This function is a helper function of create_shortened url, and will handle the generation of a link
    and ensuring it doesnt already exist
    """
