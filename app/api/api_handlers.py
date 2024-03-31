from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models import database

# This file hanldes the various API endpoints, i.e post, get

router = APIRouter()

@router.post("/shorten-url")
async def shorten_url():
    pass
    #this function will handle the shorten request

@router.get("/{short_url}")
async def redirect(short_url: str):
    pass
    #this function will redirect to the original link, from the shortlink


@router.get("/url-info/{short_url}")
async def link_info(short_url: str):
    pass
    #this function will provide the details of a link, in case it needs to be verified or updated
    #also may provide #clicks as a metric



