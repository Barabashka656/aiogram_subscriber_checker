from pydantic import BaseModel


class Article(BaseModel):
    id: int | None = None
    link: str | None = None
    title: str | None = None
    
    class Config:
        from_attributes = True

class User(BaseModel):
    user_id: int | None = None
    is_active: bool = True
    
    class Config:
        from_attributes = True
