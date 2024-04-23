
from fastapi import FastAPI, HTTPException, status, Depends, Response
from typing import Optional
from pydantic import BaseModel, HttpUrl
from app.service.url_shortener import create_shortened_url, get_redirect_url


"""
This file hanldes the various API endpoints, i.e post, get

The general flow of information is as follows:
        Customer <-> Api_handlers <-> url_shortener.py <-> database
"""
app = FastAPI()


#using BaseModel to ensure data is valid
class ShortenRequest(BaseModel):
    original_url: HttpUrl
    short_url: Optional[str] = None


class ShortenResponse(BaseModel):
    short_url: str
def get_current_username():
    """
    this is a temporary hardcode value. This function may move to another file, and will be correctly
    implemented at a later time. For now, it simulates handling a user upon link creation
    """
    return "mattcrosby87@gmail.com"

@app.post("/shorten-url", response_model=ShortenResponse, status_code=201)
async def shorten_url(request: ShortenRequest, username: str = Depends(get_current_username)) -> ShortenResponse:
    try:
        result_url = create_shortened_url(request.original_url, request.short_url, username)
        if result_url:
            return ShortenResponse(short_url=result_url)
        raise HTTPException(status_code=404, detail="Failed to create shortened URL")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/{short_url}")
async def redirect(short_url: str):
    """
    this function will take the short_url and pass it on to url_shortener.py
    if the url was found, it redirects, otherwise displays 404
    """

    url = get_redirect_url(short_url)
    if not url:
        raise HTTPException(status_code=404, detail="Url Not found")
    return Response(status_code=307, headers={"Location": url})





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