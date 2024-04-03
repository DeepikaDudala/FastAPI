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
    class Config():
        orm_mode:True

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        orm_mode =True

