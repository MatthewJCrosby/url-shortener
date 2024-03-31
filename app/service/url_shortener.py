from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.database import create_link, get_link_by_short_url

#this file handles the logic of interacting and modifying the database
router = APIRouter()

#ShortenRequest ensures the input is in the correct format (JSON)
class ShortenRequest(BaseModel):
    original_url: str


@router.post("/shorten-url")
async def shorten_url(request: ShortenRequest):
    # this function will facilitate the taking of the information and passing it along to the database
    pass

@router.get("/{short_url}")
async def redirect_to_original(short_url: str):
    # This function will facilitate the link lookup and redirect
    # If the short URL is not found, raise an HTTPException with status code 404
    pass

@router.put("/update/{short_url}")
async def update_short_url(short_url: str, new_url: str):
    # This function will update the short URL to point to a new original URL
    pass

