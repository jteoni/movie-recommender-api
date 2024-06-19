from pydantic import BaseModel, Field
from typing import Optional, List
from uuid import UUID, uuid4


class User(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    name: str
    movie_genre: List
