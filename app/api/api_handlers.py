from fastapi import FastAPI, HTTPException
from typing import Optional

"""
This file hanldes the various API endpoints, i.e post, get

The general flow of information is as follows:
        Customer <-> Api_handlers <-> url_shortener.py <-> database
"""
app = FastAPI()


@app.post("/shorten-url")
async def shorten_url():
    pass
    """
    this function will handle the shorten request API call, and pass the information to url_shortener.py. 
    Recieves a response form url_shortener.py to indicate success or failure
    """


@app.get("/{short_url}")
async def redirect(short_url: str):
    pass
    """
    this function will take the short_url and pass it on to url_shortener.py
    """


@app.get("/url-info/{short_url}")
async def link_info(short_url: str):
    pass
    """
    this function will pass the shortlink to url_shortener.py, 
    will return date created, #clicks after receiving a response

    """


@app.put("/update/{short_url}")
async def update_short_url(short_url: str, new_url: str) -> bool:
    pass
    """
    This function will take new information for an existing link and send it to url_shortener.py 
    returns a message to indicate success or failure
    """


@app.delete("/delete/{short_url")
async def delete_url(short_url: str) -> bool:
    pass
    """
    This function will take the short_url and pass it to url_shortener for verification
    """