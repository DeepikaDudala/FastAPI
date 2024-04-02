from pydantic import BaseModel


class Blog(BaseModel):
    title:str
    body:str
    published:bool = False

class UpdateBlog(BaseModel):
    published:bool