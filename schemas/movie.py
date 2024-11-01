from pydantic import BaseModel, Field
from typing import Optional, List
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(...,min_length=5, max_length=20)
    overview: str = Field(...,min_length=5, max_length=200)
    year: int = Field(...,le=2022, ge=1888)
    rating: float = Field(...,le=10, ge=1)
    category: str = Field(...,min_length=5, max_length=15)
    
    class Config:
        json_schema_extra = {
            "example" : {
                "id": 1,
                "title": 'My Movie',
                "overview": "Movies description",
                "year": 2022,
                "rating": 9.8,
                "category": "Action",
            }
        }
