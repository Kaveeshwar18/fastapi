from pydantic import BaseModel, Field

class Post(BaseModel):
    title: str = Field(min_length=3)
    content: str = Field(min_length=5)