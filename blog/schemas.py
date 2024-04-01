from pydantic import BaseModel


class Blog(BaseModel):
    title:str
    body:str
    published:bool = True
    class Config():
        orm_mode = True
