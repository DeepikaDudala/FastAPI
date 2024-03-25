from fastapi import FastAPI
from . import models
from . import schemas
from .database import engine


models.Base.metadata.create_all(engine)

app = FastAPI()



@app.post('/blog') 
def create_blog(request:schemas.Blog):
    return request