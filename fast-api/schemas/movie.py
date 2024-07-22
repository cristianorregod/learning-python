from pydantic import BaseModel, Field
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2024)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=5, max_length=15)

    def model_dump(self):
        return {
            "id": self.id,
            "title": self.title,
            "overview": self.overview,
            "year": self.year,
            "rating": self.rating,
            "category": self.category
        }

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Star Wars",
                "overview": "A long time age when you was a child this happened",
                "year": 1977,
                "rating": 7.8,
                "category": "Action"
            }
        }
