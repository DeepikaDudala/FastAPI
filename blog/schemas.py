from typing import List
from pydantic import BaseModel

class Blog(BaseModel):
    title:str
    body:str
    published:bool = False
    class Config():
        orm_mode = True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title:str
    email:str
    creator:ShowUser
    class Config():
        orm_mode =True

