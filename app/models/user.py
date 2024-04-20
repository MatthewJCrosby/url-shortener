from pydantic import BaseModel
from typing import List, Optional

class User(BaseModel):
    username: str
    links: List[str] = []  # List of short URLs
    """
    Users are saved to the UserTable
    """