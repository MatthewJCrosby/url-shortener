from pydantic import BaseModel, HttpUrl
from typing import Optional
class Link(BaseModel):
    # id: Optional[str]  # Ensure it's declared optional if it should be
    original_url: str
    short_url: Optional[str]
    clicks: int = 0