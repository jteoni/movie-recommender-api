from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4


class Movie(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4)
    name: str
    genre: str
    director: str
    year: int
    reviews: int
    audience_score: int
