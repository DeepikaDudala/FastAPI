from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def main():
    return "hello"  

@app.get('/blog')
def blogs(limit:int = 10 ,published:bool = True,sort:str|None = None):
    if published:
        return {"data":f'{limit} published blogs'}
    else:
        return {"data":f'{limit} unpublished blogs'}

@app.get('/blog/{id}')
def giveBlog(id:int):
    return {"data":id}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]=True

@app.post('/blog')
def create_blog(request:Blog):
    return {"data":request}