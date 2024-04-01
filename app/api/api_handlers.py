from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.models import database

"""
This file hanldes the various API endpoints, i.e post, get

The general flow of information is as follows:
    When a shortlink must be created:
    customer -> api_handlers -> url_shortener -> api_handlers -> database.py -> api_handlers ->  customer

    
    When a link exists, and needs to be retrieved, updated, or deleted:
    customer -> api_handlers -> database.py -> spi_handlers -> customer
"""
app = FastAPI

@app.post("/shorten-url")
async def shorten_url():
    pass
    """
    this function will handle the shorten request API call, and pass the information to url_shortener.py
    then send the returned information to database.py for permanet insertion
    """

@app.get("/{short_url}")
async def redirect(short_url: str):
    pass
    """
    this function will take the short_url and directly ask database.py for the redirect url
    """



@app.get("/url-info/{short_url}")
async def link_info(short_url: str):
    pass
    """
    this function will ask database.py for the links information such as destination, date created, #clicks
    and return it to the customer
    """


@app.put("/update/{short_url}")
async def update_short_url(short_url: str, new_url: str):
    pass
    """
    This function will take new information for an existing link and send it to database.py for updating
    returns a message to indicate success or failure
    """
