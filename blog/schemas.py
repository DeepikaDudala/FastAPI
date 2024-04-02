from pydantic import BaseModel


class Blog(BaseModel):
    title:str
    body:str
    published:bool = False
    class Config():
        orm_mode = True

class UpdateBlog(BaseModel):
    published:bool
